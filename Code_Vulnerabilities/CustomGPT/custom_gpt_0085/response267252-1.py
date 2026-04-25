
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
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _do_ping(self, host):
        results = []
        for _ in range(self.probes):
            ans, output = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt")
            if ans == 0:
                rtt = output.split('/')  # Split to get round-trip times
                results.append(float(rtt[4]))  # Take the average RTT
            time.sleep(1)
        return results

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        times = self._do_ping(host)
        for t in times:
            # Ensure only valid data is updated
            if t is not None:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(t)}')
                time.sleep(5)
        self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1h", "--vertical-label=ms",
                             "DEF:avg_rtt=%s:packets:AVERAGE" % self.rrdfile,
                             "LINE1:avg_rtt#00FF00:Avg RTT")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
