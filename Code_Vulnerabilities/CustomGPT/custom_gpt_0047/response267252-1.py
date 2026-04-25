
import rrdtool
import time
import commands
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        try:
            rrdtool.create(
                self.rrdfile,
                "--step", str(self.interval),
                "DS:packets:GAUGE:600:0:100",
                "RRA:AVERAGE:0.5:1:288",
                "RRA:AVERAGE:0.5:12:336"
            )
        except Exception as e:
            print(f"Error creating RRD: {e}")

    def get_hosts(self, user_id):
        my_hosts = hosts.query.filter_by(uid=user_id).all()
        return my_hosts.pop(0) if my_hosts else None

    def do_ping(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 1 -w 2 {host} | grep rtt")
            if status == 0:
                rtt = output.split('/')[-3]  # Get the average RTT
                self.rrdList.append(float(rtt))
            else:
                self.rrdList.append(0)  # Append zero on failure
        return self.rrdList 

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        if host:
            times = self.do_ping(host)
            for loc in times:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
                time.sleep(5)
            self.graph()

    def graph(self):
        ret = rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1",
            "--step", "300",
            "--vertical-label=ms",
            "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
            "LINE1:packets#00FF00:Ping Response Time",
            "GPRINT:packets:AVERAGE:Avg Response\: %6.2lf ms",
            "GPRINT:packets:MAX:Max Response\: %6.2lf ms"
        )
        if ret:
            print("Graph generated successfully")
        else:
            print("Failed to generate graph")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
