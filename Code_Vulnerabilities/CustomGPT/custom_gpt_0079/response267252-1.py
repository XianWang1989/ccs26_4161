
import rrdtool
import time
import subprocess
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
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:U:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:12:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for x in range(self.probes):
            result = subprocess.run(["ping", "-c", "3", "-w", "6", host],
                                    stdout=subprocess.PIPE, text=True)
            rtt_line = [line for line in result.stdout.splitlines() if "rtt" in line]
            if rtt_line:
                rtt_values = rtt_line[0].split("/")
                self.rrdList.append(rtt_values[4])
            else:
                self.rrdList.append(0)  # No response

        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for loc in times:
            if isinstance(loc, str) and loc:
                rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(float(loc))}")
            time.sleep(self.interval)
        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png", 
                      "--start", "-1", 
                      "--end", "+1", 
                      "--step", "300",
                      "--vertical-label=Bytes/s",
                      "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                      "AREA:inoctets#7113D6:In traffic",
                      "CDEF:inbits=inoctets,8,*",
                      "COMMENT:\\n",
                      "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                      "COMMENT:  ",
                      "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
