
# Function: Simple ping plotter for rrd
import rrdtool
import time
import sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile,
                           "--step", str(self.interval),
                           "DS:packets:GAUGE:600:U:U",
                           "RRA:AVERAGE:0.5:1:288")
            print("RRD file created successfully.")
        except Exception as e:
            print(f"Error creating RRD file: {e}")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        rtt_values = []
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 1 {host} | grep rtt")
            if status == 0:  # Successful ping
                rtt = output.split('/')  # Extract average RTT
                rtt_values.append(float(rtt[4]))  # RTT is the 5th element
            else:
                rtt_values.append(0)  # No response or error
        return rtt_values

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for rtt in times:
            if rtt > 0:  # Only update if RTT is valid
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')
                print(f'Updated RRD with: {int(time.time())}:{rtt}')
            time.sleep(self.interval)
        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", f"-{mins * 60}",
                      "--vertical-label=ms",
                      f"DEF:packets={self.rrdfile}:packets:AVERAGE",
                      "LINE1:packets#FF0000:RTT")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
