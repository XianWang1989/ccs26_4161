
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

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile,
                             "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, _ = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans:
                self.rrdList.append(ans)

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if host:
            self._doPing(host)
            for ping_result in self.rrdList:
                timestamp = int(time.time())
                rrdtool.update(self.rrdfile, f'{timestamp}:{int(float(ping_result))}')

            self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png",
                            "--start", str(-mins * 60),
                            "--end", "now",
                            "--step", "300",
                            "--vertical-label=Bytes/s",
                            "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                            "AREA:inoctets#7113D6:In traffic",
                            "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r",
                            "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
