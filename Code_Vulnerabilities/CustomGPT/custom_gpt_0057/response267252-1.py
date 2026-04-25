
import rrdtool
import time
import sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:GAUGE:600:0:U",
            "RRA:AVERAGE:0.5:1:288",
            "RRA:AVERAGE:0.5:12:336"
        )

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0].hostname if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if status == 0:
                self.rrdList.append(float(output))
            time.sleep(1)  # Added sleep to avoid rapid pings
        return self.rrdList

    def plotRRD(self):
        if not os.path.exists(self.rrdfile):
            self.create_rrd()
        host = self.getHosts(3)
        if host:
            times = self._doPing(host)
            for loc in times:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
            self.graph(60)

    def graph(self, mins):
        rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", f"-{mins * 60}",
            "--step", str(self.interval),
            "--vertical-label=Bytes/s",
            f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
            "AREA:inoctets#7113D6:In traffic",
            "COMMENT:\\n",
            "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r",
            "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf"
        )

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
