
# Function: Simple ping plotter for rrd
import rrdtool
import time
import sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile, "--step", str(self.interval),
                           "DS:packets:GAUGE:600:0:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:12:336")
            print("RRD file created successfully.")
        except Exception as e:
            print(f"Error creating RRD file: {e}")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(
                f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if status == 0:
                self.rrdList.append(float(output))
            else:
                self.rrdList.append(0)  # Append 0 on failure
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for loc in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
            print(f'Updated RRD with: {int(time.time())}:{loc}')
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", str(-60*mins),
                      "--step", str(self.interval),
                      "--vertical-label=Packets",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE2:packets#FF0000:Packet Traffic",
                      "COMMENT:\\n",
                      "GPRINT:packets:AVERAGE:Avg Packets\: %6.2lf",
                      "COMMENT:  ",
                      "GPRINT:packets:MAX:Max Packets\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
