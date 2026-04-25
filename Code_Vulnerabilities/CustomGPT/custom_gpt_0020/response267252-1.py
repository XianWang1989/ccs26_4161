
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
        # Print information if rrd is created successfully
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Failed to create RRD file:", rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        results = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput("ping -c 1 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
            print(f"Ping result for {host}: {ans} -- RTT: {unans}")
            if unans.strip().isnumeric():
                results.append(unans.strip())
            else:
                results.append(0)  # or handle the case differently
        return results 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        times = self._doPing(host)
        for loc in times:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f'{timestamp}:{loc}')
            print(f'Updated RRD with time: {timestamp}, packets: {loc}')
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph("%s.png" % self.rrdfile, "--start", "-1", "--end", "+1", "--step", "300",
                             "--vertical-label=Bytes/s",
                             "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                             "AREA:inoctets#7113D6:In traffic",
                             "CDEF:inbits=inoctets,8,*",
                             "COMMENT:\\n",
                             "GPRINT:inbits:AVERAGE:Avg In traffic: %6.2lf \\r",
                             "COMMENT:  ",
                             "GPRINT:inbits:MAX:Max In traffic: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
