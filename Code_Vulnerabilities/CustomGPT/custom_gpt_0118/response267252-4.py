
def graph(self, mins):
    ret = rrdtool.graph("%s.png" % self.rrdfile, "--start", "-1", "--end", "now", "--step", "300",
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                        "AREA:inoctets#7113D6:In traffic",
                        "COMMENT:\\n",
                        "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf \\r",
                        "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")

    if ret:
        print("Error generating graph:", ret)
