
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
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288")

    def fetch_host(self):
        # Assuming this method retrieves a valid hostname
        return self.getHosts(3)

    def ping_host(self, host):
        status, output = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
        if status == 0 and output:
            return float(output)
        return None

    def update_rrd(self):
        host = self.fetch_host()
        ping_time = self.ping_host(host)
        if ping_time is not None:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{ping_time}')
            print(f'Updated RRD with timestamp: {int(time.time())} and value: {ping_time}')
        else:
            print("Ping failed or returned no valid result.")

    def plot_graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", 
                      "--start", "-1h",
                      "--step", "300",
                      "--vertical-label=Ping Time (ms)",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE2:packets#FF0000:Ping Time")

    def run(self):
        self.create_rrd()
        for _ in range(self.probes):
            self.update_rrd()
            time.sleep(5)  # Allow time between probes
        self.plot_graph()

if __name__ == "__main__":
    rrd = rrdPing()
    rrd.run()
