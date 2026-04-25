
import rrdtool
import time
import commands
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.create_rrd()

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile, "--step", str(self.interval),
                           "DS:packets:GAUGE:600:U:U",
                           "RRA:AVERAGE:0.5:1:288")
            print("RRD file created.")
        except Exception as e:
            print(f"Error creating RRD: {e}")

    def get_host(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0].hostname if myHosts else None

    def _do_ping(self, host):
        rtt_values = []
        for _ in range(self.probes):
            response = commands.getstatusoutput(f"ping -c 1 -w 1 {host}")
            rtt = response[1].split('/')  # Parse the response
            if len(rtt) > 4:  # Ensure we have valid data
                rtt_values.append(float(rtt[4]))
            else:
                rtt_values.append(0)
        return rtt_values

    def plot_rrd(self):
        host = self.get_host(3)
        if host:
            times = self._do_ping(host)
            for rtt in times:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')
                print(f'Updated RRD with time {int(time.time())} and RTT {rtt}')
                time.sleep(5)
            self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1",
                      "--step", "300",
                      "--vertical-label=ms",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:packets#FF0000:RTT")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
