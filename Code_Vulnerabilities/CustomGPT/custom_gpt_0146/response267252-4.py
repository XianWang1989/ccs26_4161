
def graph(self, mins):
    last_update = rrdtool.info(self.rrdfile)['last_update']
    ret = rrdtool.graph("%s.png" % self.rrdfile, "--start", str(last_update - (mins * 60)),
                        "--end", str(last_update), "--step", "300",
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                        "AREA:inoctets#7113D6:In traffic",
                        "CDEF:inbits=inoctets,8,*",
                        "COMMENT:\\n",
                        "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                        "COMMENT:  ",
                        "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
    if ret:
        print("Graph creation error:", ret)
