
import rrdtool
import time
import subprocess

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        rrdtool.create(self.rrdfile, '--step', str(self.interval),
                       'DS:packet_loss:GAUGE:600:0:100',
                       'RRA:AVERAGE:0.5:1:288')

    def _doPing(self, host):
        try:
            output = subprocess.check_output(['ping', '-c', '3', host], universal_newlines=True)
            rtt_values = [float(line.split('/')[4]) for line in output.splitlines() if 'rtt' in line]
            self.rrdList = rtt_values
        except subprocess.CalledProcessError:
            print(f"Failed to ping {host}")
            self.rrdList.append(100)  # Assume high packet loss on failure
        return self.rrdList

    def plotRRD(self, host):
        self.create_rrd()
        for _ in range(self.probes):
            timeout = int(time.time())
            pings = self._doPing(host)
            for rtt in pings:
                rrdtool.update(self.rrdfile, f'{timeout}:{rtt}')
                print(f'Updated RRD with: {timeout}:{rtt}')
                time.sleep(5)
        self.graph()

    def graph(self):
        rrdtool.graph("traffic.png",
                      "--start", "-1h",
                      "--vertical-label=ms",
                      "DEF:packet_loss={}:packet_loss:AVERAGE".format(self.rrdfile),
                      "AREA:packet_loss#00FF00:Packet Loss",
                      "GPRINT:packet_loss:AVERAGE:Avg Packet Loss: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD('example.com')  # Replace 'example.com' with your actual host
