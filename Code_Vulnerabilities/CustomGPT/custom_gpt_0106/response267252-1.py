
import rrdtool
import time
import subprocess
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
                       "RRA:AVERAGE:0.5:6:336")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def do_ping(self, host):
        try:
            output = subprocess.check_output(f"ping -c 3 -w 6 {host}", shell=True, text=True)
            rtt = output.splitlines()[-1].split("=")[-1].split("/")[1]
            return rtt
        except subprocess.CalledProcessError:
            return None  # Return None if ping fails

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        for _ in range(self.probes):
            lat = self.do_ping(host)
            if lat is not None:
                self.rrdList.append(lat)
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{lat}')
            time.sleep(self.interval)
        self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png", 
                            "--start", "-1h", 
                            "--step", "300",
                            "--vertical-label=ms",
                            "DEF:packetav={}:packets:AVERAGE".format(self.rrdfile),
                            "LINE1:packetav#FF0000:RTT Average",
                            "GPRINT:packetav:AVERAGE:Avg RTT\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
