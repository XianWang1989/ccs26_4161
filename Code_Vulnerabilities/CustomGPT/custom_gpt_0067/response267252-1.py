
import rrdtool
import subprocess
import time
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:GAUGE:600:0:U",
            "RRA:AVERAGE:0.5:1:288"
        )

    def get_hosts(self, userID):
        my_hosts = hosts.query.filter_by(uid=userID).all()
        return my_hosts[0] if my_hosts else None

    def ping_host(self, host):
        try:
            ans = subprocess.check_output(
                ["ping", "-c", str(self.probes), host],
                universal_newlines=True
            )
            rtt = ans.splitlines()[-1].split('/')[4]  # Get average RTT
            return float(rtt)
        except Exception as e:
            print(f"Error pinging {host}: {e}")
            return None

    def update_rrd(self, rtt):
        if rtt is not None:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt}')

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)  # Replace with valid userID

        for _ in range(3):  # Pinging three times for demo
            rtt = self.ping_host(host)
            self.update_rrd(rtt)
            time.sleep(self.interval)

        self.graph()

    def graph(self):
        rrdtool.graph(
            f"{self.rrdfile}.png",
            "--start", "-1h",
            "--step", str(self.interval),
            "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
            "AREA:inoctets#7113D6:In traffic",
            "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf",
            "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf"
        )

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
