
# Function: Simple ping plotter for rrd
import rrdtool
import time
import sys
import subprocess
from model import hosts

class rrdPing:

    def __init__(self):
        self.DAY = 86400
        self.YEAR = 365 * self.DAY
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:12:336")
        if ret:
            print(rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):  # Use range for Python 3
            try:
                ans = subprocess.check_output(["ping", "-c", "1", host], stderr=subprocess.STDOUT)
                rtt = float(ans.decode().split("time=")[1].split(" ")[0])  # Extract RTT
                self.rrdList.append(rtt)
            except subprocess.CalledProcessError as e:
                print(f"Ping failed for {host}: {e.output}")
                self.rrdList.append(float('nan'))  # Append NaN for failed attempts
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for loc in times:
            if not isinstance(loc, float) or loc is None:  # Check if RTT is valid
                continue
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            print(f'Updated RRD with time: {int(time.time())}, RTT: {int(loc)}')
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", f"-{mins * 60}",
                             "--end", "now", "--step", str(self.interval),
                             "--vertical-label=ms",
                             "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                             "LINE1:packets#FF0000:Ping Time",
                             "GPRINT:packets:AVERAGE:Avg Ping\: %6.2lf ms",
                             "COMMENT:\\n",
                             "GPRINT:packets:MAX:Max Ping\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
