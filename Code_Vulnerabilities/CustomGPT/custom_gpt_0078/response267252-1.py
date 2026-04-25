
import rrdtool
import time
import subprocess
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:6:336")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def ping_host(self, host):
        cmd = f"ping -c {self.probes} -w 6 {host}"
        try:
            output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
            times = [float(line.split('/')[4]) for line in output.splitlines() if "rtt" in line]
            return times
        except subprocess.CalledProcessError as e:
            print(f"Error pinging {host}: {e}")
            return []

    def update_rrd(self, times):
        for t in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(t)}')
            time.sleep(self.interval)

    def plot_graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "now",
                      "--vertical-label=Bytes/s",
                      "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                      "AREA:inoctets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r",
                      "COMMENT:  ",
                      "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.create_rrd()
    times = ping.ping_host(ping.getHosts(3))
    if times:
        ping.update_rrd(times)
        ping.plot_graph()
        print("Graph generated successfully.")
    else:
        print("No data to plot.")
