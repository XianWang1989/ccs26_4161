
import rrdtool
import tempfile
import commands
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
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            print(f"Ping result: {unans}")  # Debugging output
            self.rrdList.append(unans)
            time.sleep(1)  # Slight delay to avoid overwhelming the host
        return self.rrdList

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for loc in times:
            try:
                # Ensure loc is valid before updating
                if loc.strip():  # Check if loc is not empty
                    rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(loc))}')
                    print(f'Updated RRD with: {int(time.time())}:{int(float(loc))}')
                else:
                    print("No valid data to update RRD.")
            except ValueError as e:
                print(f"Error while updating RRD: {e}")
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png", 
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
