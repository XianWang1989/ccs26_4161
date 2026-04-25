
import rrdtool
import time
import commands
from model import hosts

class rrdPing:

    def __init__(self, rrdfile='hostname.rrd', interval=300, probes=5):
        self.DAY = 86400
        self.YEAR = 365 * self.DAY
        self.rrdfile = rrdfile
        self.interval = interval
        self.probes = probes

    def create_rrd(self):
        if not rrdtool.info(self.rrdfile):
            rrdtool.create(self.rrdfile, "--step", "%s" % self.interval,
                           "DS:packets:COUNTER:600:U:U",
                           "RRA:AVERAGE:0.5:1:288",
                           "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def _doPing(self, host):
        rtt_list = []
        for x in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans == 0:
                rtt_list.append(unans)  # Store valid RTT responses
            else:
                print(f"Ping failed: {unans}")
        return rtt_list

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        times = self._doPing(host)

        for rtt in times:
            if rtt:
                try:
                    rtt_value = int(float(rtt))  # Ensure RTT is numeric
                    rrdtool.update(self.rrdfile, f'{int(time.time())}:{rtt_value}')
                    print(f'{int(time.time())}:{rtt_value}')
                    time.sleep(5)
                except ValueError as e:
                    print(f"Invalid RTT value: {rtt}, error: {e}")

        self.graph(60)

    def graph(self, mins):
        ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", "--step", "300",
                            "--vertical-label=Bytes/s",
                            f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                            "AREA:inoctets#7113D6:In traffic",
                            "CDEF:inbits=inoctets,8,*",
                            "COMMENT:\\n",
                            "GPRINT:inbits:AVERAGE:Avg In traffic: %6.2lf\\r",
                            "COMMENT:  ",
                            "GPRINT:inbits:MAX:Max In traffic: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
