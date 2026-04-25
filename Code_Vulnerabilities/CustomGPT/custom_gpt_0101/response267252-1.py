
# Function: Simple ping plotter for rrd
import rrdtool
import time
import commands
from model import hosts

class rrdPing:

    def __init__(self):
        self.interval = 300
        self.probes = 5
        self.rrdfile = 'hostname.rrd'
        self.create_rrd()

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _do_ping(self, host):
        results = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            results.append(unans)
        return results

    def update_rrd(self, host):
        times = self._do_ping(host)
        for loc in times:
            if loc:  # Ensure loc is not empty
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(loc))}')
            time.sleep(5)

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--step", str(self.interval),
                      "--vertical-label=ms",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:packets#FF0000:Packets Over Time")

if __name__ == "__main__":
    ping = rrdPing()
    host = ping.get_hosts(3)
    if host:
        ping.update_rrd(host)
        ping.graph()
        info = rrdtool.info('hostname.rrd')
        print(info['last_update'])
    else:
        print("No hosts found.")
