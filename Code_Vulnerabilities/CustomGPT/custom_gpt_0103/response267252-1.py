
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
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:12:336")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _do_ping(self, host):
        results = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            results.append(unans)
            time.sleep(1)  # optional delay between pings
        return results

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        if not host:
            print("No hosts found")
            return
        times = self._do_ping(host)
        for time_val in times:
            # Ensure valid numeric entries
            if time_val.isdigit():
                rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(time_val)}")
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1h",
                      "--vertical-label=Bytes/s",
                      "DEF:packets=hostname.rrd:packets:AVERAGE",
                      "AREA:packets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:packets:AVERAGE:Avg In traffic: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
