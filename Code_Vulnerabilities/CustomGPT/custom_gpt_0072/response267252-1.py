
import rrdtool
import time
import subprocess

class RRDGraph:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def ping_host(self, host):
        command = f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'"
        try:
            output = subprocess.check_output(command, shell=True, text=True)
            return float(output.strip())
        except Exception as e:
            print("Ping error:", e)
            return None

    def update_rrd(self, ping_time):
        timestamp = int(time.time())
        if ping_time is not None:
            rrdtool.update(self.rrdfile, f'{timestamp}:{ping_time}')
            print(f'Updated RRD at {timestamp} with value {ping_time}')

    def plot_rrd(self):
        self.create_rrd()
        host = "your.host.com"  # Replace with your actual host
        for _ in range(self.probes):
            ping_time = self.ping_host(host)
            self.update_rrd(ping_time)
            time.sleep(self.interval)

    def generate_graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "now",
                      "--step", str(self.interval),
                      "--vertical-label=ms",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:packets#FF0000:Packets",
                      "GPRINT:packets:AVERAGE:Avg\: %6.2lf ms")

if __name__ == "__main__":
    rrd_graph = RRDGraph()
    rrd_graph.plot_rrd()
    rrd_graph.generate_graph()
    print(rrdtool.info('hostname.rrd')['last_update'])
