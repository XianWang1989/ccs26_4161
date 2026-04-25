
import rrdtool
import commands
import time
import sys
from model import hosts

class rrdPing:
    DAY = 86400
    YEAR = 365 * DAY

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        print("Creating RRD file...")
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:U:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:6:336")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def do_ping(self, host):
        results = []
        for _ in range(self.probes):
            cmd = f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'"
            status, output = commands.getstatusoutput(cmd)
            if status == 0:
                results.append(float(output))
            else:
                print(f"Ping failed for {host}: {output}")
                results.append(None)  # Append None for failed probes
        return results 

    def update_rrd(self, values):
        for value in values:
            if value is not None:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{value}')
                print(f'Updated RRD: {int(time.time())}:{value}')
            else:
                print("No valid data to update.")

    def plot(self):
        times = self.do_ping(self.get_hosts(3))
        self.update_rrd(times)
        self.graph()

    def graph(self):
        print("Generating graph...")
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1", "--end", "now",
                      "--step", str(self.interval),
                      "--vertical-label=Bytes/s",
                      "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                      "AREA:inoctets#7113D6:In traffic",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf",
                      "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.create_rrd()  # Ensure RRD file is created before plotting
    ping.plot()
