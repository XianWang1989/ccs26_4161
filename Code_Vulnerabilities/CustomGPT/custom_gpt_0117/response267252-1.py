
import rrdtool, time, sys
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5

    def create_rrd(self):
        rrdtool.create(self.rrdfile, "--step", str(self.interval),
                       "DS:packets:COUNTER:600:U:U",
                       "RRA:AVERAGE:0.5:1:288",
                       "RRA:AVERAGE:0.5:1:336")

    def getHosts(self, userID):
        myHosts = hosts.query.filter_by(uid=userID).all()
        return myHosts[0] if myHosts else None

    def doPing(self, host):
        responses = []
        for _ in range(self.probes):
            status, output = commands.getstatusoutput(
                f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'"
            )
            if status == 0:
                responses.append(float(output))
            else:
                responses.append(0)  # Or handle the case when ping fails
        return responses

    def plotRRD(self):
        self.create_rrd()
        host = self.getHosts(3)
        if not host:
            print("No hosts found.")
            return

        times = self.doPing(host)
        for rtt in times:
            current_time = int(time.time())
            rrdtool.update(self.rrdfile, f'{current_time}:{int(rtt)}')
            time.sleep(5)
        self.graph(60)

    def graph(self, mins):
        rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", 
                      "--step", "300", "--vertical-label=Bytes/s",
                      f"DEF:packets={self.rrdfile}:packets:AVERAGE",
                      "AREA:packets#7113D6:In traffic",
                      "COMMENT:\\n",
                      "GPRINT:packets:AVERAGE:Avg Packets: %6.2lf",
                      "COMMENT:  ",
                      "GPRINT:packets:MAX:Max Packets: %6.2lf")

if __name__ == "__main__":
    ping = rrdPing()
    ping.plotRRD()
    info = rrdtool.info('hostname.rrd')
    print("Last update:", info['last_update'])
