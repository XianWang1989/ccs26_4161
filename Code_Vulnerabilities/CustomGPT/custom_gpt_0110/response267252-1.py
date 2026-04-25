
import rrdtool
import commands
import time
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:COUNTER:600:U:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        rtt_list = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if unans:  # Add check for valid response
                rtt_list.append(float(unans))
        return rtt_list

    def update_rrd(self, rtt_values):
        for rtt in rtt_values:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(rtt)}')

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if host:
            rtt_values = self._doPing(host)
            if rtt_values:
                self.update_rrd(rtt_values)
                time.sleep(5)  # Delay after updates
                self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1",
                      "--end", "+1",
                      "--step", "300",
                      "--vertical-label=ms",
                      "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                      "AREA:inoctets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf ms\\r",
                      "COMMENT:  ",
                      "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
