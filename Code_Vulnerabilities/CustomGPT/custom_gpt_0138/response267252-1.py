
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
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Error creating RRD file: ", rrdtool.error())
        else:
            print("RRD file created successfully.")

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans != 0:
                print(f"Ping error: {unans}")
                return
            self.rrdList.append(float(unans))
            time.sleep(1)

    def plotRRD(self, host):
        self.create_rrd()
        self._doPing(host)
        for loc in self.rrdList:
            rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(loc)}")
            print(f"Updated RRD with timestamp {int(time.time())} and value {int(loc)}")
            time.sleep(5)
        self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--step", "300",
                             "--vertical-label=Bytes/s",
                             f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                             "AREA:inoctets#7113D6:In traffic",
                             "CDEF:inbits=inoctets,8,*",
                             "COMMENT:\\n",
                             "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                             "COMMENT:  ",
                             "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
        if ret:
            print("Error generating graph: ", rrdtool.error())
        else:
            print("Graph generated successfully.")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD('your_host_here')  # Replace with actual host
