
import rrdtool
import time
import sys
from model import hosts  # Ensure this module is correctly implemented

class rrdPing:

    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def _doPing(self, host):
        results = []
        for _ in range(self.probes):
            ans, result = subprocess.getstatusoutput(f"ping -c 3 -w 6 {host} | grep 'rtt' | awk -F '/' '{{print $5}}'")
            if ans == 0:
                results.append(float(result))
            else:
                print(f"Ping failed for {host}: {result}")
                results.append(0)  # Append 0 or handle as needed
        return results

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)  # Replace with valid userID
        if host:
            times = self._doPing(host)
            for loc in times:
                timestamp = int(time.time())
                rrdtool.update(self.rrdfile, f'{timestamp}:{loc}')
                print(f'Updated RRD with timestamp {timestamp} and value {loc}')
                time.sleep(self.interval)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", f"-{mins * 60}", "--step", "300",
                      "--vertical-label=Bytes/s",
                      f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                      "AREA:inoctets#7113D6:In traffic",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
