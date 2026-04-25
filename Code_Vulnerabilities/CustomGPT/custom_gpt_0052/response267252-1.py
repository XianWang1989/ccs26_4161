
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
        ret = rrdtool.create(self.rrdfile,
                             "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Error creating RRD file: ", rrdtool.error())

    def get_hosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        if myHosts:
            return myHosts[0].hostname  # Assuming hostname is your field
        return None

    def do_ping(self, host):
        for _ in range(self.probes):
            try:
                ans = subprocess.check_output(["ping", "-c", "3", "-w", "6", host])
                rtt = ans.decode().splitlines()[-1].split('/')[-2]
                self.rrdList.append(float(rtt))
            except Exception as e:
                print(f"Error pinging {host}: {e}")
                self.rrdList.append(0)  # Default to 0 if ping fails

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        if not host:
            print("No host found.")
            return

        self.do_ping(host)
        for rtt in self.rrdList:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f"{timestamp}:{int(rtt)}")
            time.sleep(5)  # Sleep if you want to simulate actual intervals

        self.graph()

    def graph(self):
        ret = rrdtool.graph(f"{self.rrdfile}.png",
                            "--start", "-1",
                            "--end", "+1",
                            "--step", "300",
                            "--vertical-label=ms",
                            "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                            "AREA:packets#7113D6:Ping Time",
                            "COMMENT:\\n",
                            "GPRINT:packets:AVERAGE:Avg Ping\: %6.2lf ms",
                            "COMMENT:  ",
                            "GPRINT:packets:MAX:Max Ping\: %6.2lf ms")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
