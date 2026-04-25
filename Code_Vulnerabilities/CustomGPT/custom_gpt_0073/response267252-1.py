
import rrdtool
import subprocess
import time
import sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        for _ in range(self.probes):
            result = subprocess.run(
                ["ping", "-c", "3", "-w", "6", host],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                # Extract RTT from the output
                rtt_line = next(line for line in result.stdout.splitlines() if "rtt" in line)
                rtt = float(rtt_line.split('/')[4])  # Get the average RTT
                self.rrdList.append(rtt)
            else:
                print(f"Ping failed for {host}: {result.stderr}")

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)  # Adjust userID as needed
        self._doPing(host)
        for loc in self.rrdList:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", "--step", "300",
                      "--vertical-label=Bytes/s",
                      f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                      "AREA:inoctets#7113D6:In traffic",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic: %6.2lf",
                      "COMMENT:  ",
                      "GPRINT:inoctets:MAX:Max In traffic: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
