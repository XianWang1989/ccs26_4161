
import rrdtool
import time
import sys
from model import hosts
import subprocess

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:12:336")
        if ret:
            print(f"Error creating RRD: {rrdtool.error()}")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0].hostname if myHosts else None

    def _doPing(self, host):
        results = []
        for _ in range(self.probes):
            try:
                output = subprocess.check_output(
                    ["ping", "-c", "1", host],
                    universal_newlines=True
                )
                rtt = float(output.split('time=')[1].split(' ms')[0])  # Extract RTT
                results.append(rtt)
            except subprocess.CalledProcessError:
                results.append(None)  # Append None if ping fails
        return results 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if not host:
            print("No hosts found.")
            return

        times = self._doPing(host)
        for loc in times:
            if loc is not None:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
                print(f'{int(time.time())}:{int(loc)}')
                time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1",
                      "--end", "+1", "--step", "300",
                      "--vertical-label=Bytes/s",
                      f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                      "AREA:inoctets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r",
                      "COMMENT:  ",
                      "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
