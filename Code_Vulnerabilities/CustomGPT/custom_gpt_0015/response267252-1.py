
import rrdtool
import time
import subprocess  # Use subprocess instead of commands (deprecated)

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile, 
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:1:336")

    def do_ping(self, host):
        results = []
        for _ in range(self.probes):
            try:
                ans = subprocess.check_output(
                    ["ping", "-c", "3", host],
                    universal_newlines=True
                )
                # Extracting round-trip time
                rtt = ans.split('\n')[-2].split('/')[4]  # 5th field is avg
                results.append(rtt)
            except subprocess.CalledProcessError as e:
                print(f"Error pinging {host}: {e}")
                results.append(0)
        return results

    def plot_rrd(self):
        self.create_rrd()
        host = "example.com"  # Replace with appropriate host ID
        times = self.do_ping(host)
        for loc in times:
            if loc:  # Only update if loc is not None
                rrdtool.update(self.rrdfile, f"{int(time.time())}:{loc}")
                print(f"{int(time.time())}:{loc}")
                time.sleep(5)

        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1h",
                      "--step", "300",
                      "--vertical-label=ms",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "AREA:packets#7113D6:Ping time",
                      "COMMENT:\\n",
                      "GPRINT:packets:AVERAGE:Avg Ping\: %6.2lf ms",
                      "COMMENT:  ",
                      "GPRINT:packets:MAX:Max Ping\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
