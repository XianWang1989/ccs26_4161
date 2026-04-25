
import rrdtool
import commands
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
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Error creating RRD:", ret)

    def get_host(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _do_ping(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if status != 0:
                print(f"Ping failed for {host}: {output}")
                self.rrdList.append(0)  # Use 0 or a suitable value if ping fails
            else:
                self.rrdList.append(float(output) if output else 0)
        return self.rrdList 

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_host(3)
        if host:
            self._do_ping(host)
            for loc in self.rrdList:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
                time.sleep(5)
            self.graph(60)
        else:
            print("No host found.")

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", f"-{mins}m", "--step", str(self.interval),
                            "--vertical-label=ms",
                            f"DEF:packets={self.rrdfile}:packets:AVERAGE",
                            "LINE1:packets#FF0000:Packet Loss")
        if ret:
            print("Error generating graph:", ret)

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print("Last update time:", info['last_update'])
