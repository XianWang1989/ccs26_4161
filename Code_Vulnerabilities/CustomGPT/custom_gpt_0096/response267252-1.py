
def create_rrd(self, interval):
    ret = rrdtool.create(
        self.rrdfile,
        "--step", str(self.interval),
        "DS:packets:COUNTER:600:U:U",
        "RRA:AVERAGE:0.5:1:288",
        "RRA:AVERAGE:0.5:1:336"
    )
    if ret:
        print("Error creating RRD:", rrdtool.error())
