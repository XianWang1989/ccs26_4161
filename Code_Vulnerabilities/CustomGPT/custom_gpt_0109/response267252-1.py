
import rrdtool
import tempfile
import subprocess
import time
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

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:12:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            try:
                result = subprocess.check_output(
                    ["ping", "-c", "3", "-w", "6", host], text=True)
                rtt = result.splitlines()[-1].split()[3].split('/')[1]
                self.rrdList.append(rtt)
            except Exception as e:
                print(f"Error pinging {host}: {e}")
                self.rrdList.append(0)  # Append 0 if ping fails
        return self.rrdList 

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for loc in times:
            timestamp = int(time.time())
            if loc:  # Check if loc is a valid RTT value
                rrdtool.update(self.rrdfile, f'{timestamp}:{loc}')
                print(f'{timestamp}:{loc}')
            time.sleep(self.interval)

        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png",
                            "--start", f"-{mins * 60}",
                            "--end", "now",
                            "--step", str(self.interval),
                            "--vertical-label=ms",
                            "DEF:packets=hostname.rrd:packets:AVERAGE",
                            "AREA:packets#7113D6:Latency",
                            "CDEF:inbits=packets,8,*",
                            "COMMENT:\\n",
                            "GPRINT:inbits:AVERAGE:Avg Latency\: %6.2lf ms \\r",
                            "COMMENT:  ",
                            "GPRINT:inbits:MAX:Max Latency\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
