
import rrdtool
import time
import commands
import sys
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
                       "RRA:AVERAGE:0.5:1:288",  # 2 days worth of data
                       "RRA:AVERAGE:0.5:6:336")  # 7 days worth of data

    def get_host(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0].hostname if myHosts else None

    def do_ping(self, host):
        rtt_list = []
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if status == 0:
                rtt_list.append(float(output))
        return rtt_list

    def update_rrd(self):
        host = self.get_host(3)
        if host:
            rtt_times = self.do_ping(host)
            for rtt in rtt_times:
                rrdtool.update(self.rrdfile, f"N:{rtt}")

    def plot_rrd(self):
        self.create_rrd()
        self.update_rrd()
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1h",
                      "--step", str(self.interval),
                      "--vertical-label=RTT (ms)",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE2:packets#FF0000:Ping RTT")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
