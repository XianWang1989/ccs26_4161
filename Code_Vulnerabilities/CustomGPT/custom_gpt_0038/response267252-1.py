
# Function: Simple ping plotter for rrd
import rrdtool
import time
import sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        if not os.path.exists(self.rrdfile):
            rrdtool.create(self.rrdfile, "--step", str(self.interval),
                           "DS:packets:GAUGE:600:0:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 1 -w 5 {host} | grep rtt")
            if status == 0:
                # Extract the round trip time (RTT)
                rtt = output.split('=')[1].split('/')[0].strip()
                self.rrdList.append(float(rtt))
            else:
                self.rrdList.append(0)  # Append 0 if ping fails
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if host:
            times = self._doPing(host)
            for loc in times:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
                time.sleep(5)
            self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-{mins * 60}", "--end", "now", "--step", "300",
                      "--vertical-label=Bytes/s",
                      "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                      "AREA:inoctets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r",
                      "COMMENT:  ",
                      "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
