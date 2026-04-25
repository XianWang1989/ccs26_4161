
import rrdtool
import time
import commands  # Use subprocess for Python 3
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:COUNTER:600:U:U",
            "RRA:AVERAGE:0.5:1:288",
            "RRA:AVERAGE:0.5:1:336"
        )
        if ret:
            print("Error creating RRD:", ret)

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans == 0:  # Successful ping
                self.rrdList.append(unans)
            else:
                print(f"Error pinging {host}: {unans}")
        return self.rrdList

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for loc in times:
            timestamp = int(time.time())
            try:
                rrdtool.update(self.rrdfile, f'{timestamp}:{int(float(loc))}')
                print(f'Updated {self.rrdfile} with {timestamp}:{int(float(loc))}')
            except Exception as e:
                print("Failed to update RRD:", e)
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1",
            "--end", "+1",
            "--step", "300",
            "--vertical-label=Bytes/s",
            f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
            "AREA:inoctets#7113D6:In traffic",
            "CDEF:inbits=inoctets,8,*",
            "COMMENT:\\n",
            "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r"
        )
        if ret:
            print("Error creating graph:", ret)

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
