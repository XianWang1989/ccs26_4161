
import rrdtool
import subprocess
import time
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _do_ping(self, host):
        responses = []
        for _ in range(self.probes):
            try:
                output = subprocess.check_output(
                    ["ping", "-c", "3", host],
                    stderr=subprocess.STDOUT, universal_newlines=True
                )
                rtt = output.split("avg=")[-1].split("/")[0]
                responses.append(float(rtt))  # Get average RTT
            except subprocess.CalledProcessError as e:
                responses.append(0)  # Handle unreachable host
        return responses

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        times = self._do_ping(host)
        for rtt in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1h",
                      "--vertical-label=ms",
                      "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:inoctets#FF0000:Ping Time",
                      "GPRINT:inoctets:AVERAGE:Avg Ping\: %6.2lf ms",
                      "GPRINT:inoctets:MAX:Max Ping\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
