
import rrdtool
import subprocess
import time
from model import hosts

class RRDPing:
    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:1:336")

    def _do_ping(self, host):
        pings = []
        for _ in range(self.probes):
            result = subprocess.run(["ping", "-c", "3", "-w", "6", host], capture_output=True, text=True)
            if result.returncode == 0:
                # Extract the average RTT
                avg_rtt = self.extract_avg_rtt(result.stdout)
                pings.append(avg_rtt)
            else:
                print(f"Ping failed for {host}")
                pings.append(0)  # Append zero for failed pings
        return pings

    def extract_avg_rtt(self, output):
        for line in output.splitlines():
            if "rtt" in line:
                return float(line.split('/')[4])  # Get the average RTT
        return 0

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        times = self._do_ping(host)
        for rtt in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph("traffic.png",
                      "--start", "-1",
                      "--end", "now",
                      "--step", "300",
                      "--vertical-label=ms",
                      "DEF:packets=hostname.rrd:packets:AVERAGE",
                      "LINE:packets#FF0000:Packets")

    def get_hosts(self, user_id):
        # Assuming this method retrieves hosts based on user ID
        return hosts.query.filter_by(uid=user_id).first().hostname

if __name__ == "__main__":
    ping = RRDPing()
    ping.plot_rrd()
