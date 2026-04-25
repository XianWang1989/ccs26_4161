
import subprocess
import rrdtool
import time
from model import hosts

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
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print(f"Error Creating RRD: {rrdtool.error()}")

    def _doPing(self, host):
        for _ in range(self.probes):
            ans = subprocess.run(["ping", "-c", "3", "-w", "6", host], capture_output=True, text=True)
            if ans.returncode == 0:
                rtt_line = [line for line in ans.stdout.splitlines() if 'avg' in line]
                if rtt_line:
                    rtt_value = float(rtt_line[0].split('/')[4])
                    self.rrdList.append(rtt_value)
            else:
                print(f"Ping failed for {host}: {ans.stderr}")
            time.sleep(1)

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        self._doPing(host)
        for loc in self.rrdList:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", str(-mins * 60), "--end", "now",
                             "--step", "300",
                             "--vertical-label=ms",
                             "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                             "AREA:inoctets#7113D6:In traffic",
                             "COMMENT:\\n",
                             "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf ms\\r",
                             "COMMENT:  ",
                             "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf ms")
        if ret:
            print(f"Error Creating Graph: {rrdtool.error()}")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
