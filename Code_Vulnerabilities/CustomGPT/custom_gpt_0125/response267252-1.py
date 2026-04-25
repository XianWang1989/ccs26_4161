
# Function: Simple ping plotter for rrd
import rrdtool, tempfile, commands, time, sys
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

    def create_rrd(self, interval):
        ret = rrdtool.create("%s" % self.rrdfile, "--step", "%s" % self.interval,
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for x in range(self.probes):
            ans, unans = commands.getstatusoutput(
                "ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host
            )
            print(x)
            self.probes -= 1
            self.rrdList.append(unans)
        return self.rrdList

    def plotRRD(self):
        self.create_rrd(self.interval)
        times = self._doPing(self.getHosts(3))
        for x in range(len(times)):
            loc = times.pop(0)
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print('%d:%d' % (int(time.time()), int(float(loc))))
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph("%s.png" % self.rrdfile, "--start", "-1", "--end", "+1", "--step", "300",
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
