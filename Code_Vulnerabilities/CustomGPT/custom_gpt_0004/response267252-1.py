
import rrdtool
import time
import commands
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
                       "RRA:AVERAGE:0.5:1:288")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if unans:  # Check if the output is valid
                self.rrdList.append(float(unans))
        return self.rrdList

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if host:
            times = self._doPing(host)
            for packet_loss in times:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{packet_loss}')
                time.sleep(5)
            self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1h", "--step", "300",
                      "--vertical-label=Bytes/s",
                      "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                      "AREA:inoctets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r",
                      "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
