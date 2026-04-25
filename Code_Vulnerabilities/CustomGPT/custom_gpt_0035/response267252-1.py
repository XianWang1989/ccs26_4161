
import rrdtool
import time
import sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

        # Create RRD file if it doesn't exist
        if not os.path.exists(self.rrdfile):
            self.create_rrd()

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:COUNTER:600:U:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:1:336")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if output.strip():
                self.rrdList.append(output.strip())
        return self.rrdList

    def plotRRD(self):
        times = self._doPing(self.get_hosts(3))
        for elapsed in times:
            if elapsed:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{elapsed}')
                time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1",
                      "--end", "+1",
                      "--step", "300",
                      "--vertical-label=Bytes/s",
                      f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                      "AREA:inoctets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic: %6.2lf \\r")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
