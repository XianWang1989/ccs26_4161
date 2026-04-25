
import rrdtool
import time
import commands

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:GAUGE:600:0:U",
            "RRA:AVERAGE:0.5:1:288"
        )

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 1 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if unans:
                self.rrdList.append(float(unans))
            time.sleep(1)
        return self.rrdList 

    def plotRRD(self, host):
        self.create_rrd()
        times = self._doPing(host)

        for loc in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
            time.sleep(self.interval)

        self.graph()

    def graph(self):
        rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1h",
            "--vertical-label=ms",
            "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
            "LINE1:packets#00FF00:Ping Time"
        )

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD('example.com')  # Replace with your target host
