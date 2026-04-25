
import rrdtool
import time
import commands

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
            print("Error creating RRD file:", ret)

    def do_ping(self, host):
        results = []
        for _ in range(self.probes):
            cmd = f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'"
            _, unans = commands.getstatusoutput(cmd)
            if unans:
                results.append(float(unans))
                print(f"Pinging {host}: {unans} ms")
            else:
                print(f"Ping failed for {host}")
        return results

    def plot_rrd(self, host):
        self.create_rrd()
        times = self.do_ping(host)
        for lat in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{lat}')
            print(f'Updated RRD with timestamp {int(time.time())} and latency {lat}')
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1", "--step", "300",
                      "--vertical-label=ms",
                      f"DEF:latency={self.rrdfile}:packets:AVERAGE",
                      "LINE:latency#FF0000:Latency",
                      "GPRINT:latency:AVERAGE:Average Latency\: %6.2lf ms\\r",
                      "GPRINT:latency:MAX:Max Latency\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd("your_hostname_here")
