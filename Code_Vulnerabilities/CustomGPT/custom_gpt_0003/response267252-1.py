
import rrdtool
import time
import sys
from model import hosts   # Make sure the 'hosts' model is imported correctly.

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

        # Create RRD only once
        self.create_rrd()

    def create_rrd(self):
        ret = rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:GAUGE:600:0:U",  # Change COUNTER to GAUGE for packet loss
            "RRA:AVERAGE:0.5:1:288",
            "RRA:AVERAGE:0.5:1:336"
        )
        if ret is not None:
            print(rrdtool.error())

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        valid_responses = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            # Only append valid response times
            if ans == 0 and unans:  # Successful ping
                valid_responses.append(float(unans))
            time.sleep(1)  # Optional delay to avoid ping flooding
        return valid_responses

    def plotRRD(self):
        host = self.getHosts(3)
        if host is None:
            print("No hosts found.")
            return

        times = self._doPing(host)
        for latency in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{latency}')  # Update RRD file
            time.sleep(self.interval)

        self.graph(60)

    def graph(self, mins):
        output = rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", f"-{mins * 60}",
            "--end", "now",
            "--step", str(self.interval),
            "--vertical-label=ms",
            "DEF:latency=%s:packets:AVERAGE" % self.rrdfile,
            "AREA:latency#7113D6:Ping Times",
            "GPRINT:latency:AVERAGE:Avg Latency: %6.2lf ms",
            "GPRINT:latency:MAX:Max Latency: %6.2lf ms"
        )
        if output is not None:
            print(rrdtool.error())

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
