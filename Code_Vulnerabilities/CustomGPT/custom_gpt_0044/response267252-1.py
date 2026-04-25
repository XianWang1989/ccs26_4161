
import rrdtool
import time
import commands
from model import hosts

class rrdPing:
    def __init__(self):
        self.rrdfile = 'hostname.rrd'
        self.interval = 300
        self.probes = 5
        self.rrdList = []

    def create_rrd(self):
        ret = rrdtool.create(
            self.rrdfile,
            '--step', str(self.interval),
            'DS:packets:COUNTER:600:U:U',
            'RRA:AVERAGE:0.5:1:288',
            'RRA:AVERAGE:0.5:12:336'
        )
        if ret:
            print("Error creating RRD:", rrdtool.error())

    def get_hosts(self, user_id):
        my_hosts = hosts.query.filter_by(uid=user_id).all()
        return my_hosts[0].hostname if my_hosts else None

    def do_ping(self, host):
        response_times = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if unans:
                response_times.append(float(unans))
        return response_times 

    def plot_rrd(self):
        self.create_rrd()
        host = self.get_hosts(3)
        times = self.do_ping(host)
        for response_time in times:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f'{timestamp}:{int(response_time)}')
            time.sleep(5)
        self.graph()

    def graph(self):
        ret = rrdtool.graph(
            f"{self.rrdfile}.png",
            '--start', '-1', '--end', '+1',
            '--step', '300',
            '--vertical-label=ms',
            f'DEF:inoctets={self.rrdfile}:packets:AVERAGE',
            'AREA:inoctets#7113D6:In traffic',
            'CDEF:inbits=inoctets,8,*',
            'COMMENT:\\n',
            'GPRINT:inbits:AVERAGE:Avg In traffic: %6.2lf ms\\r',
            'GPRINT:inbits:MAX:Max In traffic: %6.2lf ms'
        )
        if ret:
            print("Error creating graph:", rrdtool.error())

if __name__ == "__main__":
    ping = rrdPing()
    ping.plot_rrd()
    info = rrdtool.info('hostname.rrd')
    print(info['last_update'])
