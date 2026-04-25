
import rrdtool
import commands
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
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:COUNTER:600:0:U",
                             "RRA:AVERAGE:0.5:1:288")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0]

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans == 0:
                self.rrdList.append(float(unans))
            else:
                print(f"Error pinging {host}: {unans}")
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        times = self._doPing(host)
        for loc in times:
            rrdtool.update(self.rrdfile, f'N:{loc}')
            print(f'Updated RRD with: N:{loc}')
            time.sleep(5)
        self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png",
                            "--start", "-1h",  # Last hour
                            "--step", str(self.interval),
                            "--vertical-label=Bytes/s",
                            f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                            "LINE2:inoctets#FF0000:In traffic",
                            "COMMENT:\\n",
                            "GPRINT:inoctets:AVERAGE:Avg In traffic: %6.2lf Bytes/s")

        if ret:
            print("Error generating graph:", rrdtool.error())

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
