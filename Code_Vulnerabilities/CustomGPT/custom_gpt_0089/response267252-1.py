
import rrdtool
import time
import commands

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    # Create RRD file
    def create_rrd(self):
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:1:336")

    # Ping and gather data
    def doPing(self, host):
        for _ in range(self.probes):
            ...
            # Ensure output is handled correctly
            ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
            if unans:  # Check if unans is not empty
                self.rrdList.append(float(unans))
            else:
                print(f"Failed to get response from {host}")

    # Update RRD and plot
    def plotRRD(self, host):
        if not os.path.exists(self.rrdfile):
            self.create_rrd()

        self.doPing(host)

        for loc in self.rrdList:
            rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(loc)}")

        self.graph()

    # Create graph
    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1h",  # last hour
                      "--vertical-label=Packets",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:packets#00FF00:Packets",
                      "COMMENT:\\n",
                      "GPRINT:packets:AVERAGE:Avg Packets\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD("your_hostname_here")
