
import rrdtool
import tempfile
import time
import sys
from model import hosts
sys.path.append('/home/dirk/devel/python/stattool/stattool/lib')
import nurrd
from nurrd import RRDplot

class rrdPing(RRDplot):
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
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(
                f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans == 0:
                self.rrdList.append(unans)  # Successfully pinged
            else:
                self.rrdList.append(0)  # Defaulting to 0 if ping failed
        return self.rrdList

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for loc in times:
            try:
                loc_value = float(loc)
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc_value)}')
                print(f'Updated RRD with: {int(time.time())}:{int(loc_value)}')
            except ValueError:
                print(f"Invalid ping value: {loc}")
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", "--step", "300",
                            "--vertical-label=Bytes/s",
                            f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                            "AREA:inoctets#7113D6:In traffic",
                            "CDEF:inbits=inoctets,8,*",
                            "COMMENT:\\n",
                            "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                            "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print("Last update:", info['last_update'])
