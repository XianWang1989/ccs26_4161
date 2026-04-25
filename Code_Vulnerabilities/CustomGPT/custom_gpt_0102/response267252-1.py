
import rrdtool
import subprocess
import time
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",  # Use GAUGE for packet loss
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:12:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        command = ["ping", "-c", str(self.probes), host]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            times = [float(line.split('/')[4]) for line in result.stdout.splitlines() if "rtt" in line]
            return times[-1] if times else 0
        return 0

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        loc = self._doPing(host)
        if loc:
            rrdtool.update(self.rrdfile, f'N:{loc}')  # Use 'N' to update with the last value
            time.sleep(self.interval)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1h", "--step", "300",
                      "--title=", "Ping Response Time",
                      "--vertical-label=Time (ms)",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:packets#00FF00:Avg Response Time",
                      "GPRINT:packets:AVERAGE:Avg\: %6.2lf ms",
                      "GPRINT:packets:MAX:Max\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
