
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
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Error creating RRD file:", rrdtool.error())

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def do_ping(self, host):
        results = []
        for _ in range(self.probes):
            try:
                output = subprocess.check_output(f"ping -c 3 -w 6 {host}", shell=True)
                rtt = output.decode().strip().split('\n')[-1].split('/')[4]
                results.append(rtt)
            except subprocess.CalledProcessError as e:
                print(f"Ping failed: {e}")
                results.append(0)  # Default to 0 if ping fails
        return results

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        response_times = self.do_ping(host)

        for rtt in response_times:
            current_time = int(time.time())
            rrdtool.update(self.rrdfile, f'{current_time}:{rtt}')
            print(f'Updated RRD with time {current_time} and RTT {rtt}')
            time.sleep(5)

        self.graph()

    def graph(self):
        ret = rrdtool.graph("output.png",
                             "--start", "-3600",   # last hour
                             "--step", str(self.interval),
                             "--vertical-label=Bytes/s",
                             "DEF:packets={}:packets:AVERAGE".format(self.rrdfile),
                             "LINE1:packets#00FF00:Packets",
                             "GPRINT:packets:AVERAGE:Avg Packets: %6.2lf",
                             "COMMENT:\\n")
        if ret:
            print("Error creating graph:", rrdtool.error())

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
