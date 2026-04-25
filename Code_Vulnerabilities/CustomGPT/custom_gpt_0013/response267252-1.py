
import rrdtool
import time
import sys
import subprocess
from model import hosts

class rrdPing:

    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile,
                             "--step", str(self.interval),
                             "DS:packets:COUNTER:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:12:336")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            try:
                result = subprocess.check_output(
                    ["ping", "-c", "3", "-w", "6", host],
                    text=True
                )
                rtt = [line for line in result.splitlines() if "rtt" in line]
                if rtt:
                    avg_rtt = float(rtt[0].split("/")[4])
                    self.rrdList.append(avg_rtt)
                else:
                    self.rrdList.append(0)  # Handle no response
            except Exception as e:
                print(f"Error pinging {host}: {e}")
                self.rrdList.append(0)  # Append zero if there's an error

    def plotRRD(self):
        self.create_rrd()
        self._doPing(self.getHosts(3))
        for loc in self.rrdList:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f'{timestamp}:{loc}')
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1",
                      "--end", "+1",
                      "--step", "300",
                      "--vertical-label=Bytes/s",
                      f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
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
