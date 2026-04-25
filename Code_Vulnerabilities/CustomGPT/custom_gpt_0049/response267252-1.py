
import rrdtool
import time
import commands
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
        if ret:
            print("Error creating RRD: ", ret)

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        rrd_times = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans == 0:
                rrd_times.append(float(unans))
            else:
                print(f"Ping failed for {host}: {unans}")
        return rrd_times 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if not host:
            print("No valid host found!")
            return

        times = self._doPing(host)
        for loc in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end" , "+1", "--step", "300",
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
