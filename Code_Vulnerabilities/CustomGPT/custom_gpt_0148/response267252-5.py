
import rrdtool
import subprocess
import time

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:GAUGE:600:U:U",
            "RRA:AVERAGE:0.5:1:288",
            "RRA:AVERAGE:0.5:1:336"
        )
        return ret

    def _doPing(self, host):
        for _ in range(self.probes):
            result = subprocess.run(
                ["ping", "-c", "3", host],
                stdout=subprocess.PIPE,
                text=True
            )
            rtt = self.extract_rtt(result.stdout)
            self.rrdList.append(rtt)
        return self.rrdList

    def extract_rtt(self, output):
        for line in output.splitlines():
            if 'rtt' in line:
                return float(line.split('/')[4])
        return None

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing('example.com')  # Replace with your host
        for loc in times:
            if loc is not None:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png",
                     "--start", f"-{mins * 60}",
                     "--vertical-label=ms",
                     "DEF:rtt=%s:packets:AVERAGE" % self.rrdfile,
                     "LINE2:rtt#FF0000:RTT",
                     "GPRINT:rtt:AVERAGE:Avg RTT: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
