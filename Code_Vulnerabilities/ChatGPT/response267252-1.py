
import rrdtool
import time
import commands
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:GAUGE:600:U:U",  # Change COUNTER to GAUGE for packet loss
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:12:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        rtt_list = []
        for _ in range(self.probes):
            ret, output = commands.getstatusoutput(f"ping -c 1 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ret == 0:  # Ping successful
                rtt_list.append(float(output))  # Store round-trip time
            else:
                print(f"Ping failed: {output}")
                rtt_list.append(float('nan'))  # Append NaN if ping fails
        return rtt_list 

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))
        for timestamp, rtt in zip(range(int(time.time()), int(time.time()) + len(times) * self.interval, self.interval),
                                   times):
            if rtt is not None and not (rtt != rtt):  # Avoid NaN
                rrdtool.update(self.rrdfile, f'{timestamp}:{rtt}')
                print(f'Updated RRD with: {timestamp}:{rtt}')
            time.sleep(1)  # Delay to avoid excessive calls
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1h",  # last hour
                      "--vertical-label=RTT (ms)",
                      "DEF:rtt=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE1:rtt#FF0000:RTT",
                      "COMMENT:\\n",
                      "GPRINT:rtt:AVERAGE:Avg RTT: %6.2lf ms",
                      "GPRINT:rtt:MAX:Max RTT: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
