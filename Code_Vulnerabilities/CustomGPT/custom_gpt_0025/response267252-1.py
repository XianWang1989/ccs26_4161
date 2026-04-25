
# Function: Simple ping plotter for RRD
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
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:5:288")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 1 -w 6 {host} | grep rtt")
            if status == 0:
                rtt = output.split('/')[4]  # Extracting the average RTT
                self.rrdList.append(float(rtt))
            else:
                self.rrdList.append(0)  # Consider 0 if ping fails
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        times = self._doPing(host)

        for loc in times:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f'{timestamp}:{loc}')
            time.sleep(self.interval)  # Respect the interval

        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", f"-{mins * 60}",
                      "--step", str(self.interval),
                      "--vertical-label=RTT (ms)",
                      "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                      "AREA:inoctets#7113D6:RTT",
                      "GPRINT:inoctets:AVERAGE:Avg RTT: %6.2f ms\\n",
                      "GPRINT:inoctets:MAX:Max RTT: %6.2f ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
