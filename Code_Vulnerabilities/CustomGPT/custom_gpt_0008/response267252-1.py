
# Function: Simple ping plotter for rrd
import rrdtool
import time
import commands

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",  # Changed to GAUGE
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:5:288")

    def _doPing(self, host):
        rtt_list = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            print(f"Ping output: {unans}")  # Print output for debugging
            try:
                rtt = float(unans)  # Convert to float
                rtt_list.append(rtt)
            except ValueError:
                rtt_list.append(0)  # Append 0 on error
        return rtt_list

    def plotRRD(self, host):
        self.create_rrd()
        rtt_times = self._doPing(host)
        for rtt in rtt_times:
            timestamp = int(time.time())
            print(f"Updating RRD at {timestamp} with value {rtt}")
            rrdtool.update(self.rrdfile, f'{timestamp}:{rtt}')
            time.sleep(5)
        self.graph()

    def graph(self):
        print("Generating graph...")
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1", "--end", "+1",
                      "--step", "300",
                      "--vertical-label=ms",
                      "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:inoctets#7113D6:RTT")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD('your_target_host')
