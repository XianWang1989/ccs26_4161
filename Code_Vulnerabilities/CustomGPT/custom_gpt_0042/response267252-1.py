
# Function: Simple ping plotter for rrd
import rrdtool
import time
import sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:GAUGE:600:0:U",
            "RRA:AVERAGE:0.5:1:288"
        )

    def get_hosts(self, userID):
        my_hosts = hosts.query.filter_by(uid=userID).all()
        return my_hosts.pop(0) if my_hosts else None

    def do_ping(self, host):
        rtt_list = []
        for _ in range(self.probes):
            status, output = os.popen(f"ping -c 1 -W 1 {host}").read().strip().split('\n')[-1].split('/')
            if status == 0:
                rtt_list.append(float(output[4]))  # Round Trip Time
            else:
                rtt_list.append(0)  # No response
            time.sleep(1)  # Wait 1 second between pings
        return rtt_list

    def update_rrd(self, rtt_values):
        for rtt in rtt_values:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        if host:
            rtt_values = self.do_ping(host)
            self.update_rrd(rtt_values)
            self.graph()

    def graph(self):
        rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1h",
            "--vertical-label=Response Time (ms)",
            "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
            "LINE1:packets#FF0000:Ping Response Time",
            "GPRINT:packets:AVERAGE:Avg Response Time\: %6.2lf ms",
            "GPRINT:packets:MAX:Max Response Time\: %6.2lf ms\\n"
        )

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print("Last update:", info['last_update'])
