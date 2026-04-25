
import rrdtool
import subprocess
import time
import sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        try:
            rrdtool.create(self.rrdfile, "--step", str(self.interval),
                           "DS:packets:COUNTER:600:U:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:1:336")
        except Exception as e:
            print(f"Error creating RRD: {e}")

    def _doPing(self, host):
        for x in range(self.probes):
            try:
                result = subprocess.check_output(
                    ["ping", "-c", "3", host],
                    stderr=subprocess.STDOUT,
                    universal_newlines=True
                )
                rtt = result.split('time=')[1].split(' ')[0]
                self.rrdList.append(rtt)
            except subprocess.CalledProcessError:
                self.rrdList.append('0')  # handle failed ping

    def plotRRD(self):
        self.create_rrd()
        self._doPing(self.getHosts(3))
        for rtt in self.rrdList:
            if rtt:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(rtt))}')

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
