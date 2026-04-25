
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
        ret = rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:COUNTER:600:U:U",
            "RRA:AVERAGE:0.5:1:288",
            "RRA:AVERAGE:0.5:1:336"
        )
        if ret:
            print("Error creating RRD file:", rrdtool.error())

    def do_ping(self, host):
        rtt_list = []
        for _ in range(self.probes):
            ret, output = commands.getstatusoutput(f"ping -c 1 -w 2 {host} | grep rtt | awk -F '/' '{{print $5}}'")
            if ret == 0:  # Ping was successful
                rtt_list.append(output)
            else:
                print(f"Ping failed for {host}: {output}")
            time.sleep(1)
        return rtt_list

    def update_rrd(self):
        times = self.do_ping(self.get_hosts())
        for rtt in times:
            if rtt:
                rtt_value = float(rtt)
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(rtt_value)}')
                print(f'Updated {self.rrdfile} with {int(rtt_value)} at time {int(time.time())}')
            else:
                print("No RTT value to update.")

    def get_hosts(self):
        myHosts = hosts.query.filter_by(uid=3).all()
        return myHosts[0].hostname if myHosts else None

    def plot_graph(self):
        rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1h",
            "--step", str(self.interval),
            "--vertical-label=Milliseconds",
            f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
            "LINE1:inoctets#FF0000:RTT"
        )

if __name__ == "__main__":
    ping = rrdPing()
    ping.create_rrd()
    ping.update_rrd()
    ping.plot_graph()
