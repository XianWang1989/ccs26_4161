
import rrdtool
import subprocess
import time
import sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.DAY = 86400
        self.YEAR = 365 * self.DAY
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

        # Check if RRD file exists, if not create it
        self.create_rrd()

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile, "--step", str(self.interval),
                           "DS:packets:COUNTER:600:0:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:12:336")
        except rrdtool.OperationalError as e:
            print(f"Error creating RRD: {e}")

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def _do_ping(self, host):
        results = []
        for _ in range(self.probes):
            try:
                output = subprocess.check_output(f"ping -c 3 -w 6 {host}", shell=True, text=True)
                rtt_line = next(line for line in output.splitlines() if 'rtt' in line)
                rtt_value = float(rtt_line.split('/')[4])
                results.append(rtt_value)
            except Exception as e:
                print(f"Ping failed for {host}: {e}")
                results.append(0)  # Append 0 or some default value on error
        return results

    def plot_rrd(self):
        times = self._do_ping(self.get_hosts(3))
        for loc in times:
            try:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
                print(f'Updated RRD with value: {loc} at {time.time()}')
                time.sleep(5)
            except Exception as e:
                print(f"Failed to update RRD: {e}")

        self.graph()

    def graph(self):
        try:
            rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1h", "--end", "now", "--step", str(self.interval),
                          "--vertical-label=ms",
                          f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                          "LINE1:inoctets#FF0000:In traffic",
                          "COMMENT:\\n",
                          "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf ms")

        except Exception as e:
            print(f"Failed to create graph: {e}")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
