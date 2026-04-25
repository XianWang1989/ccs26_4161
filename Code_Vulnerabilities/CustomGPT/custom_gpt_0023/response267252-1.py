
import rrdtool
import time
import sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile, 
                           "--step", str(self.interval),
                           "DS:packets:COUNTER:600:U:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:1:336")
            print("RRD file created.")
        except Exception as e:
            print("Error creating RRD file:", str(e))

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        results = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if unans:
                results.append(float(unans))
            else:
                print(f"Ping failed for host: {host}")
        return results

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if not host:
            print("No hosts found for user.")
            return

        times = self._doPing(host)
        for loc in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            print(f'Updated: {int(time.time())}:{int(loc)}')
            time.sleep(5)

        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", 
                      "--start", "-1", "--step", "300",
                      "--vertical-label=Bytes/s",
                      f"DEF:inoctets={self.rrdfile}:packets:AVERAGE", 
                      "AREA:inoctets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r",
                      "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(f"Last update: {info['last_update']}")
