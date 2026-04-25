
# Function: Simple ping plotter for rrd
import rrdtool
import time
import sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []
        self.create_rrd()

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:U:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 1 -w 5 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans == 0:  # Success
                self.rrdList.append(float(unans))
        return self.rrdList 

    def plotRRD(self):
        times = self._doPing(self.getHosts(3))
        for loc in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", "--step", "300",
                      "--vertical-label=ms",
                      "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                      "LINE3:inoctets#FF0000:Ping Time",
                      "GPRINT:inoctets:AVERAGE:Avg Ping\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
