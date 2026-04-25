
import rrdtool
import tempfile
import subprocess
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
        ret = rrdtool.create(self.rrdfile, 
                             "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            command = f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'"
            ans = subprocess.getoutput(command)
            self.rrdList.append(ans.strip())
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if host is None:
            print("No hosts found.")
            return
        times = self._doPing(host)

        for loc in times:
            if loc:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(loc))}')
                print(f'{int(time.time())}:{int(float(loc))}')
                time.sleep(5)

        self.graph()

    def graph(self):
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

        if ret:
            print("Error creating graph:", rrdtool.error())

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
