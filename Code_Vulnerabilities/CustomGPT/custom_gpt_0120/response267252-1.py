
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
        ret = rrdtool.create(self.rrdfile,
                             "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:12:336")
        if ret:
            print("Error creating RRD file:", rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, _ = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            print(f"Ping response: {ans}")
            if ans:
                self.rrdList.append(float(ans))
            else:
                self.rrdList.append(0)
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if host:
            times = self._doPing(host)
            for loc in times:
                timestamp = int(time.time())
                rrdtool.update(self.rrdfile, f"{timestamp}:{loc}")
                print(f"Updated RRD with: {timestamp}:{loc}")
                time.sleep(self.interval)
            self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png",
                            "--start", f"-{mins}m",
                            "--end", "now",
                            "--step", str(self.interval),
                            "--vertical-label=Bytes/s",
                            "DEF:inoctets=hostname.rrd:packets:AVERAGE",
                            "LINE2:inoctets#00FF00:Packets",
                            "COMMENT:\\n",
                            "GPRINT:inoctets:AVERAGE:Avg Packets: %6.2lf",
                            "GPRINT:inoctets:MAX:Max Packets: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
