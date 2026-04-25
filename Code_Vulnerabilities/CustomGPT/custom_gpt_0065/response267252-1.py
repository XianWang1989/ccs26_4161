
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
                             "RRA:AVERAGE:0.5:1:288")
        if ret:
            print("Error creating RRD:", ret)

    def _doPing(self, host):
        results = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if unans:  
                results.append(float(unans))
            else:
                print(f"Ping failed for {host}")
                results.append(0)  # Use 0 or another value for the update
        return results

    def update_rrd(self, values):
        for value in values:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(value)}')

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png",
                            "--start", "-1", "--end", "now",
                            "--step", str(self.interval),
                            "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                            "AREA:inoctets#7113D6:In traffic",
                            "GPRINT:inoctets:AVERAGE:Avg In traffic: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.create_rrd()
    times = ping._doPing("your_host_here")  # Replace with the actual host
    ping.update_rrd(times)
    ping.graph()
