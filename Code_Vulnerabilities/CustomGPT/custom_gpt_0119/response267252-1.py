
import rrdtool
import time
import commands  # Note: in Python 3, use subprocess instead of commands

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288")

    def _doPing(self, host):
        results = []
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 1 -W 1 {host} | grep rtt")
            if status == 0 and output:
                # Extract RTT value
                rtt = output.split("/")[4]  # Get the average RTT
                results.append(float(rtt))
            else:
                results.append(0)  # No response
        return results 

    def plotRRD(self, host):
        self.create_rrd()
        times = self._doPing(host)
        for rtt in times:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f"{timestamp}:{rtt}")
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--step", str(self.interval),
                      "--vertical-label=ms",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:packets#FF0000:RTT",
                      "GPRINT:packets:AVERAGE:Avg RTT\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD("example.com")  # Replace with your target host
