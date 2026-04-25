
import rrdtool
import time
import sys
from model import hosts
import subprocess  # Changed from commands to subprocess

class rrdPing:
    def __init__(self):
        self.DAY = 86400
        self.YEAR = 365 * self.DAY
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:U:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:10:288")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        for _ in range(self.probes):
            result = subprocess.run(
                ["ping", "-c", "3", "-w", "6", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            rtt_line = [line for line in result.stdout.splitlines() if "rtt" in line]
            if rtt_line:
                rtt = rtt_line[0].split('/')[4]
                self.rrdList.append(float(rtt))
            else:
                self.rrdList.append(0.0)  # Handle cases where ping fails
        return self.rrdList

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if host:
            times = self._doPing(host)
            for rtt in times:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')
                time.sleep(5)
            self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1",
                      "--step", str(self.interval),
                      "--vertical-label=ms",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:packets#FF0000:Avg packet response time",
                      "GPRINT:packets:AVERAGE:Avg Response Time\: %6.2lf ms\\n",
                      "GPRINT:packets:MAX:Max Response Time\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print("Last Update:", info['last_update'])
