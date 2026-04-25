
# Function: Simple ping plotter for rrd
import rrdtool
import time
import commands
from model import hosts
sys.path.append('/home/dirk/devel/python/stattool/stattool/lib')
from nurrd import RRDplot

class rrdPing(RRDplot):

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []
        self.create_rrd()

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            self.rrdList.append(unans if ans == 0 else 0)  # Capture actual response time or 0 on failure
        return self.rrdList 

    def plotRRD(self):
        self.rrdList = self._doPing(self.getHosts(3))
        for loc in self.rrdList:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1",
                      "--step", "300",
                      "--vertical-label=ms",
                      "DEF:response_time=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:response_time#FF0000:Response Time",
                      "GPRINT:response_time:AVERAGE:Avg\: %6.2lf ms",
                      "GPRINT:response_time:MAX:Max\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
