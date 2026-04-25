
import rrdtool
import time
import subprocess
import sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(self.rrdfile,
                             "--step", "300",
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288")
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0) if myHosts else None

    def do_ping(self, host):
        for _ in range(self.probes):
            try:
                result = subprocess.run(
                    ["ping", "-c", "3", "-w", "6", host],
                    capture_output=True, text=True
                )
                rtt_line = [line for line in result.stdout.split('\n') if 'rtt' in line]
                if rtt_line:
                    rtt = rtt_line[0].split('/')[4]
                    self.rrdList.append(float(rtt))
                else:
                    self.rrdList.append(None)  # Handle no response
            except Exception as e:
                print(f"Ping error for {host}: {str(e)}")
        return self.rrdList 

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        if not host:
            print("No hosts found.")
            return

        times = self.do_ping(host)
        for loc in times:
            if loc is not None:  # Only update for valid RTT values
                if rrdtool.update(self.rrdfile, f'N:{loc}'):
                    print("Error updating RRD:", rrdtool.error())
            time.sleep(5)

        self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png",
                            "--start", "-1h",
                            "--vertical-label=ms",
                            "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                            "LINE1:inoctets#00FF00:RTT")

        if ret:
            print("Error generating graph:", rrdtool.error())

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info.get('last_update', 'No update info'))
