
import rrdtool
import time
import commands
from model import hosts

class rrdPing:
    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:12:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput("ping -c 1 -w 1 {}".format(host))
            if status == 0:
                rtt = output.split('/')[-3]  # Extract RTT
                self.rrdList.append(float(rtt))
            else:
                self.rrdList.append(0)
        return self.rrdList

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if host:
            times = self._doPing(host)
            for loc in times:
                rrdtool.update(self.rrdfile, "{}:{}".format(int(time.time()), loc))
                time.sleep(5)
            self.graph()

    def graph(self):
        rrdtool.graph("{}.png".format(self.rrdfile),
                      "--start", "-1h",
                      "--vertical-label=Packets",
                      "DEF:packets={}:packets:AVERAGE".format(self.rrdfile),
                      "LINE1:packets#FF0000:Packets",
                      "GPRINT:packets:AVERAGE:Avg\: %6.2lf",
                      "GPRINT:packets:MAX:Max\: %6.2lf",
                      "COMMENT:\\n")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
