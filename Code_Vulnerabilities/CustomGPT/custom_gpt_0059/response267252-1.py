
# Function: Simple ping plotter for rrd
import rrdtool
import time
import os
from model import hosts

class rrdPing:
    def __init__(self):
        self.DAY = 86400
        self.YEAR = 365 * self.DAY
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        if not os.path.exists(self.rrdfile):
            rrdtool.create(
                self.rrdfile,
                "--step", str(self.interval),
                "DS:packets:GAUGE:600:0:U",
                "RRA:AVERAGE:0.5:1:288",
                "RRA:AVERAGE:0.5:6:336"
            )

    def _doPing(self, host):
        latencies = []
        for _ in range(self.probes):
            try:
                ans = os.popen(f"ping -c 1 -W 1 {host} | grep rtt").read()
                if ans:
                    latency = float(ans.split('/')[4])
                    latencies.append(latency)
                else:
                    latencies.append(None)
            except Exception as e:
                latencies.append(None)

        return latencies

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for latency in times:
            if latency is not None:
                rrdtool.update(self.rrdfile, f"{int(time.time())}:{latency}")
                time.sleep(5)  # Adjust based on probe interval

        self.graph()

    def graph(self):
        rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1h",  # Last hour
            "--step", str(self.interval),
            "--vertical-label=Latency (ms)",
            "DEF:latency=%s:packets:AVERAGE" % self.rrdfile,
            "LINE1:latency#FF0000:Latency",
            "COMMENT:\\n",
            "GPRINT:latency:AVERAGE:Avg Latency: %6.2lf ms",
            "GPRINT:latency:MAX:Max Latency: %6.2lf ms"
        )

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
