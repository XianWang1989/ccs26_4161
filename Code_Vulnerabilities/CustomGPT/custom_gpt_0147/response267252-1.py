
# Function: Simple ping plotter for rrd
import rrdtool
import time
import sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.DAY = 86400
        self.YEAR = 365 * self.DAY
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        try:
            rrdtool.create(
                self.rrdfile,
                "--step", str(self.interval),
                "DS:packets:GAUGE:600:0:U",
                "RRA:AVERAGE:0.5:1:288",
                "RRA:AVERAGE:0.5:1:336"
            )
        except Exception as e:
            print(f"Error creating RRD file: {e}")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):  # Use range instead of xrange for Python 3
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans == 0:  # Successful ping
                self.rrdList.append(unans)
            else:
                print(f"Ping error for host {host}: {unans}")
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        times = self._doPing(host)
        current_time = int(time.time())
        for loc in times:
            try:
                if loc:  # Ensure loc is not empty
                    rrdtool.update(self.rrdfile, f'{current_time}:{int(float(loc))}')
                    print(f'Updated RRD with: {current_time}:{int(float(loc))}')
            except Exception as e:
                print(f"Error updating RRD: {e}")
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        try:
            rrdtool.graph(
                f"{self.rrdfile}.png",
                "--start", f"-{mins}min",
                "--vertical-label=Packets/s",
                "DEF:packets={}:packets:AVERAGE".format(self.rrdfile),
                "LINE1:packets#00FF00:Incoming Packets",
                "COMMENT:\\n",
                "GPRINT:packets:AVERAGE:Avg Packets: %6.2lf",
                "GPRINT:packets:MAX:Max Packets: %6.2lf"
            )
        except Exception as e:
            print(f"Graphing error: {e}")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
