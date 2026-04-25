
# Function: Simple ping plotter for rrd
import rrdtool, tempfile, subprocess, time, sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        # Check if RRD file already exists
        if not os.path.exists(self.rrdfile):
            rrdtool.create(self.rrdfile, "--step", str(self.interval),
                           "DS:packets:GAUGE:600:0:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:1:336")

    def _doPing(self, host):
        for _ in range(self.probes):
            try:
                output = subprocess.check_output(f"ping -c 3 -w 6 {host}",
                                                  shell=True, universal_newlines=True)
                rtt_line = next(line for line in output.splitlines() if "rtt" in line)
                rtt_value = float(rtt_line.split('/')[4])
                self.rrdList.append(rtt_value)
            except Exception as e:
                print(f"Ping failed: {e}")
                self.rrdList.append(0)  # Append 0 on failure
        return self.rrdList

    def plotRRD(self):
        self.create_rrd()
        times = self._doPing(self.getHosts(3))  # Ensure getHosts returns a valid host
        for value in times:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f'{timestamp}:{value}')
            print(f'{timestamp}:{value}')
            time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", "--step", "300",
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
