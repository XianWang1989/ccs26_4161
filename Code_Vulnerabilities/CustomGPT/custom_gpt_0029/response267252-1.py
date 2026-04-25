
import rrdtool
import time
import commands

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile, "--step", str(self.interval),
                           "DS:packets:GAUGE:600:0:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:12:336")
        except Exception as e:
            print(f"Error creating RRD: {e}")

    def _doPing(self, host):
        for _ in range(self.probes):
            try:
                result = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
                if result[0] == 0:  # Successful ping
                    self.rrdList.append(float(result[1].strip()))
                else:
                    self.rrdList.append(0)  # Append 0 for failed ping
            except Exception as e:
                print(f"Error during ping: {e}")
                self.rrdList.append(0)
        return self.rrdList

    def update_rrd(self):
        for latency in self._doPing('your_hostname'):
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{latency}')
            time.sleep(5)

    def plot(self):
        self.create_rrd()
        self.update_rrd()
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1h", "--title=Ping Response Times",
                      "--vertical-label=Latency (ms)",
                      "DEF:latency=hostname.rrd:packets:AVERAGE",
                      "LINE1:latency#00FF00:Response Time")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot()
