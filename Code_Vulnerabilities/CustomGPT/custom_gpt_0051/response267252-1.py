
import rrdtool
import time
import sys
import subprocess
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:U:U",
                       "RRA:AVERAGE:0.5:1:288")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def _do_ping(self, host):
        rtt_list = []
        for _ in range(self.probes):
            output = subprocess.check_output(["ping", "-c", "1", host])
            rtt = self.extract_rtt(output)
            if rtt:
                rtt_list.append(rtt)
        return rtt_list 

    def extract_rtt(self, ping_output):
        try:
            lines = ping_output.decode('utf-8').split('\n')
            for line in lines:
                if "time=" in line:
                    return float(line.split("time=")[1].split()[0])
        except Exception as e:
            print(f"Error extracting RTT: {e}")
        return None

    def update_rrd(self, rtt):
        if rtt is not None:
            rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(rtt)}")

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        if not host:
            print("No hosts found.")
            return
        rtts = self._do_ping(host)
        for rtt in rtts:
            self.update_rrd(rtt)
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph("output.png", "--start", "-1h", "--vertical-label=ms",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:packets#FF0000:RTT",
                      "GPRINT:packets:AVERAGE:Avg RTT\: %6.2lf ms\\n",
                      "GPRINT:packets:MAX:Max RTT\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
