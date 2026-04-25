
import rrdtool
import commands
import time
import sys
from model import hosts

class rrdPing:

    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        try:
            ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                                 "DS:packets:COUNTER:600:0:U",
                                 "RRA:AVERAGE:0.5:1:288",
                                 "RRA:AVERAGE:0.5:1:336")
            if ret:
                print("Error creating RRD:", rrdtool.error())
        except Exception as e:
            print(f"Exception occurred: {e}")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts.pop(0)

    def _doPing(self, host):
        rtt_list = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 1 -w 2 {host} | grep 'time='")
            if ans == 0:
                time_value = unans.split('time=')[1].split(' ')[0]
                rtt_list.append(float(time_value))
            else:
                rtt_list.append(None)  # Append None for failed requests
        return rtt_list 

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)  # Change user ID accordingly
        times = self._doPing(host)

        for loc in times:
            if loc is not None:  # Only update with valid data
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
                print(f'Updating RRD with timestamp: {int(time.time())} and value: {int(loc)}')
            time.sleep(5)

        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--step", "300",
                      "--vertical-label=Bytes/s",
                      f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                      "AREA:inoctets#7113D6:In traffic",
                      "CDEF:inbits=inoctets,8,*",
                      "COMMENT:\\n",
                      "GPRINT:inbits:AVERAGE:Avg In traffic: %6.2lf",
                      "COMMENT:  ",
                      "GPRINT:inbits:MAX:Max In traffic: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
