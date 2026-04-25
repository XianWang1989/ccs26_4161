
import rrdtool
import time
import commands
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0].hostname if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if unans:
                self.rrdList.append(float(unans))
            else:
                self.rrdList.append(0)  # Ensure we add something even if the ping fails
        return self.rrdList 

    def plotRRD(self):
        if not self.rrdList:
            self.create_rrd()

        host = self.getHosts(3)
        if not host:
            print("No host found.")
            return

        times = self._doPing(host)
        for loc in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", "--step", "300",
                      "--vertical-label=Bytes/s",
                      "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                      "AREA:inoctets#7113D6:In traffic",
                      "CDEF:inbits=inoctets,8,*",
                      "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                      "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print("Last update:", info['last_update'])
