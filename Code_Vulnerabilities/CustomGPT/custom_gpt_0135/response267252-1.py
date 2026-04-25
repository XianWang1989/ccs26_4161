
import rrdtool
import time
import commands
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
                             "RRA:AVERAGE:0.5:1:288")
        if ret:
            print("Error creating RRD:", ret)

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0].address if myHosts else None

    def _do_ping(self, host):
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 1 {host} | grep rtt")
            if status == 0:
                rtt = float(output.split('/')[4])
                self.rrdList.append(rtt)
                print(f"Ping time: {rtt} ms")
            else:
                self.rrdList.append(0)  # Log failure with 0
        return self.rrdList 

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        if not host:
            print("No host found!")
            return

        times = self._do_ping(host)
        for rtt in times:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')
            print(f'Updated RRD with time: {int(time.time())} and rtt: {rtt}')
            time.sleep(5)
        self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-600", "--vertical-label=ms",
                            "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                            "LINE1:inoctets#FF0000:Ping Time",
                            "GPRINT:inoctets:AVERAGE:Avg Ping Time\: %6.2lf ms",
                            "GPRINT:inoctets:MAX:Max Ping Time\: %6.2lf ms")
        if ret:
            print("Error creating graph:", ret)

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
