
import rrdtool
import time
import commands
from model import hosts

class RRDGraph:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:GAUGE:600:0:U",
            "RRA:AVERAGE:0.5:1:288",
            "RRA:AVERAGE:0.5:6:336"
        )

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _do_ping(self, host):
        rtt_values = []
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if output:
                rtt_values.append(float(output))
        return rtt_values

    def update_rrd(self):
        host = self.get_hosts(3)
        if host:
            times = self._do_ping(host)
            for rtt in times:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')
                time.sleep(5)

    def plot_rrd(self):
        self.create_rrd()
        self.update_rrd()
        rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1h",
            "--step", "300",
            "--vertical-label=RTT (ms)",
            "DEF:rtt={}:packets:AVERAGE".format(self.rrdfile),
            "LINE2:rtt#FF0000:RTT",
            "GPRINT:rtt:AVERAGE:Avg RTT: %6.2lf ms",
            "GPRINT:rtt:MAX:Max RTT: %6.2lf ms"
        )

if __name__ == "__main__":
    graph = RRDGraph()
    graph.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print("Last update:", info['last_update'])
