
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
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:12:336")
        if ret:
            print("Error creating RRD:", rrdtool.error())
        else:
            print("RRD created successfully.")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _do_ping(self, host):
        responses = []
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt")
            if status == 0:
                rtt = output.split('/')[4]
                responses.append(rtt)
            else:
                print(f"Ping failed for {host}: {output}")
                responses.append(0)  # Append 0 for failed probes
            time.sleep(1)
        return responses

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        if host:
            times = self._do_ping(host)
            for loc in times:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
            self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--step", "300",
                            "--vertical-label=ms",
                            "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                            "LINE1:packets#FF0000:Ping time",
                            "GPRINT:packets:AVERAGE:Avg Ping\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
