
import rrdtool
import time
import commands

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:GAUGE:600:0:U",
            "RRA:AVERAGE:0.5:1:288"
        )

    def do_ping(self, host):
        ping_results = []
        for _ in range(self.probes):
            ans, _ = commands.getstatusoutput(f"ping -c 1 {host} | grep rtt")
            if ans:
                reply = ans.split('/')  # parse the result
                ping_results.append(float(reply[4]))  # get the avg RTT
        return ping_results

    def update_rrd(self, times):
        for lat in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{lat}')
            time.sleep(1)  # sleep for a second between updates

    def plot_rrd(self):
        self.create_rrd()
        host = "example.com"  # Change to your host
        times = self.do_ping(host)
        self.update_rrd(times)
        rrdtool.graph("output.png", 
                      "--start", "-1h", 
                      "--title=RRD Graph", 
                      "--vertical-label=RTT (ms)", 
                      "DEF:latency=hostname.rrd:packets:AVERAGE", 
                      "LINE2:latency#FF0000:Average RTT")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
