
import rrdtool
import subprocess
import time
from model import hosts

class rrdPing:

    def __init__(self):
        self.DAY = 86400
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:COUNTER:600:0:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:12:336")

    def get_host(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _do_ping(self, host):
        try:
            result = subprocess.run(
                ["ping", "-c", "3", "-w", "6", host],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                # Extract round-trip time
                rtt = result.stdout.splitlines()[-1].split('/')[4]  # median RTT
                return float(rtt)
            else:
                print(f"Ping failed for {host}: {result.stderr}")
                return None
        except Exception as e:
            print(f"Error during ping: {e}")
            return None

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_host(3)
        if not host:
            print("No host found.")
            return

        for _ in range(self.probes):
            rtt = self._do_ping(host)
            if rtt is not None:
                rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(rtt)}")
            else:
                print("Invalid RTT value.")
            time.sleep(5)

        self.graph()

    def graph(self):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1",
                      "--step", "300", "--vertical-label=Bytes/s",
                      "DEF:inoctets={}:packets:AVERAGE".format(self.rrdfile),
                      "LINE:inoctets#00FF00:In traffic",
                      "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf",
                      "COMMENT:\\n")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
