
import rrdtool
import commands
import time
import sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.probes = 5

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile, "--step", "300",
                           "DS:packets:GAUGE:600:0:U",
                           "RRA:AVERAGE:0.5:1:288")
        except Exception as e:
            print("Error creating RRD file:", e)

    def _doPing(self, host):
        rtt_values = []
        for _ in range(self.probes):
            status, output = commands.getstatusoutput("ping -c 1 -w 5 %s | grep rtt" % host)
            if status == 0:
                rtt = output.split('/')[-3]  # Get the average round trip time
                rtt_values.append(float(rtt))
            else:
                print(f"Ping failed for {host}: {output}")
        return rtt_values

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)  # Adjust as necessary
        times = self._doPing(host)
        for time_val in times:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f'{timestamp}:{time_val}')
            print(f'Updated RRD with timestamp {timestamp} and value {time_val}')
            time.sleep(5)
        self.graph()

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0].host_name if myHosts else None

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png",
                      "--start", "-1d", 
                      "--step", "300",
                      "--vertical-label=ms",
                      "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                      "LINE:packets#FF0000:Packets")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
