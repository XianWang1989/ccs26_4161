
import rrdtool
import subprocess
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
        rrdtool.create(self.rrdfile,
                       "--step", str(self.interval),
                       "DS:packets:GAUGE:600:0:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:1:336")

    def get_host(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0).hostname  # Ensure to retrieve the hostname

    def _do_ping(self, host):
        for _ in range(self.probes):
            try:
                result = subprocess.check_output(
                    ["ping", "-c", "3", "-w", "6", host],
                    stderr=subprocess.STDOUT, universal_newlines=True)
                rtt_line = [line for line in result.splitlines() if 'rtt' in line]
                rtt = float(rtt_line[0].split('/')[4]) if rtt_line else None
                self.rrdList.append(rtt)
            except subprocess.CalledProcessError as e:
                print(f"Ping failed: {e.output}")

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_host(3)
        self._do_ping(host)

        for loc in self.rrdList:
            if loc is not None:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')

        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", f"-{mins * 60}",
                      "--end", "now",
                      "--step", "300",
                      "--vertical-label=Bytes/s",
                      f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                      "AREA:inoctets#7113D6:In traffic",
                      "CDEF:inbits=inoctets,8,*",
                      "COMMENT:\\n",
                      "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                      "COMMENT:  ",
                      "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
