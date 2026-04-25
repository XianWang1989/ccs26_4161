
def graph(self, mins):
    ret = rrdtool.graph(
        "%s.png" % self.rrdfile,
        "--start", f"-{mins * 60}",
        "--end", "now",
        "--step", "300",
        "--vertical-label=ms",
        "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
        "LINE2:packets#7113D6:Response Time",
        "COMMENT:\\n",
        "GPRINT:packets:AVERAGE:Avg Response Time\: %6.2lf ms\\r",
        "GPRINT:packets:MAX:Max Response Time\: %6.2lf ms\\r"
    )
    if ret:
        print("Error generating graph:", ret)
