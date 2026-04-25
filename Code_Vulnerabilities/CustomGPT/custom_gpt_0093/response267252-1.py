
import rrdtool
import time
import commands

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.create_rrd()

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile,
                           "--step", str(self.interval),
                           "DS:packets:COUNTER:600:U:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:1:336")
        except Exception as e:
            print("Error creating RRD file:", str(e))

    def _doPing(self, host):
        rtt_list = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt")
            print(f"Output: {unans}")  # Debugging line
            if "rtt" in unans:
                rtt = unans.split('/')[-3]  # Get the average time
                rtt_list.append(rtt)
            time.sleep(1)
        return rtt_list

    def update_rrd(self, rtt_values):
        for rtt in rtt_values:
            try:
                rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(float(rtt))}")
                time.sleep(5)
            except Exception as e:
                print("Error updating RRD:", str(e))

    def plotRRD(self, host):
        rtt_values = self._doPing(host)
        self.update_rrd(rtt_values)
        self.graph()

    def graph(self):
        try:
            rrdtool.graph(f"{self.rrdfile}.png",
                          "--start", "-1",
                          "--vertical-label=ms",
                          "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                          "LINE1:inoctets#FF0000:Ping Time",
                          "GPRINT:inoctets:AVERAGE:Avg: %6.2lf")
        except Exception as e:
            print("Error generating graph:", str(e))

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD("your_host_here")  # Replace with the host you want to ping
