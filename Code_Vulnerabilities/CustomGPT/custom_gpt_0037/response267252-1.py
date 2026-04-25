
import rrdtool
import time
import sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile, "--step", str(self.interval),
                           "DS:packets:GAUGE:600:0:U",
                           "RRA:AVERAGE:0.5:1:288")
        except Exception as e:
            print(f"Error creating RRD: {e}")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _do_ping(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if unans:  # Ensure unans has a value
                self.rrdList.append(unans)
            else:
                self.rrdList.append(0)  # Fallback if ping fails
        return self.rrdList 

    def plot_rrd(self):
        self.create_rrd()
        times = self._do_ping(self.get_hosts(3))
        for loc in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(loc))}')
            time.sleep(5)
        self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "now",
                            "--vertical-label=Packets",
                            "DEF:packets=hostname.rrd:packets:AVERAGE",
                            "LINE1:packets#FF0000:Packets")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    print(rrdtool.info('hostname.rrd')['last_update'])
