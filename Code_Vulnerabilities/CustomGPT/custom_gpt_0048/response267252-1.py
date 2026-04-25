
import rrdtool
import time
import commands
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288")
        if ret:
            print(rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        rtt_list = []
        for _ in range(self.probes):
            ans, output = commands.getstatusoutput(f"ping -c 1 -W 1 {host} | grep rtt")
            if ans == 0:
                rtt = output.split('/')[-3]  # Get the average round-trip time
                rtt_list.append(float(rtt))
            else:
                rtt_list.append(0)  # Default to 0 if ping fails
        return rtt_list

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        times = self._doPing(host)
        for rtt in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')
            time.sleep(self.interval)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1 hour", "--step", "60",
                      "--vertical-label=ms",
                      "DEF:packets={}:packets:AVERAGE".format(self.rrdfile),
                      "LINE1:packets#FF0000:Ping Time")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
