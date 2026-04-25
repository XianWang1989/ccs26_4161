
def create_rrd(self):
    ret = rrdtool.create(
        self.rrdfile,
        "--step", str(self.interval),
        "DS:packets:COUNTER:600:U:U",
        "RRA:AVERAGE:0.5:1:288",
        "RRA:AVERAGE:0.5:1:336"
    )
    if ret:
        print("Error creating RRD:", rrdtool.error())

def _doPing(self, host):
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput(
            "ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host
        )
        print("Ping output:", unans)
        if 'unreachable' in unans.lower():
            continue
        self.rrdList.append(unans)
    return self.rrdList
