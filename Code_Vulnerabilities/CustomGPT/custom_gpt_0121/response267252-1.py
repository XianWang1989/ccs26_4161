
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
        try:
            rrdtool.create(
                self.rrdfile,
                "--step", str(self.interval),
                "DS:packets:COUNTER:600:0:U",
                "RRA:AVERAGE:0.5:1:288",
                "RRA:AVERAGE:0.5:12:336"
            )
            print("RRD file created successfully.")
        except Exception as e:
            print(f"Failed to create RRD file: {e}")

    def _do_ping(self, host):
        result = []
        for _ in range(self.probes):
            ans, _ = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            try:
                result.append(float(ans))
            except ValueError:
                print(f"Failed to parse ping output: {ans}")
        return result

    def update_rrd(self, times):
        for loc in times:
            if loc >= 0:
                rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(loc)}")
                print(f"Updated RRD with: {int(time.time())}:{int(loc)}")
            time.sleep(5)

    def plot(self):
        self.create_rrd()
        host = self.get_hosts(3)
        times = self._do_ping(host)
        self.update_rrd(times)
        self.graph()

    def graph(self):
        rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1h",
            "--vertical-label=Packets",
            "DEF:packets={}:packets:AVERAGE".format(self.rrdfile),
            "LINE1:packets#FF0000:Packets"
        )
        print("Graph generated.")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot()
