
import rrdtool
import time
import subprocess
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

        # Create RRD if it doesn't exist
        if not os.path.exists(self.rrdfile):
            self.create_rrd()

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:6:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            try:
                ans = subprocess.check_output(["ping", "-c", "3", "-w", "6", host])
                rtt = ans.decode().splitlines()[-1]
                # Extract the RTT value
                loc = float(rtt.split('/')[-3])  # Median RTT
                self.rrdList.append(loc)
            except subprocess.CalledProcessError as e:
                print(f"Error pinging {host}: {e}")
                self.rrdList.append(0)  # Or handle the error accordingly
        return self.rrdList

    def plotRRD(self):
        times = self._doPing(self.getHosts(3))
        for loc in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            print(f'{int(time.time())}:{loc}')
            time.sleep(self.interval)

        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", f"-{mins}m", "--step", "300",
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
    print(f"Last update: {info['last_update']}")
