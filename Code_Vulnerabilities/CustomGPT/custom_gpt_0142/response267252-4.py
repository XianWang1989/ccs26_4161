
def graph(self, mins):
    ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", "--step", "300",
                         "--vertical-label=Bytes/s",
                         "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                         "AREA:inoctets#7113D6:In traffic",
                         "CDEF:inbits=inoctets,8,*",
                         "COMMENT:\\n",
                         "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                         "COMMENT:  ",
                         "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
    if ret:
        print("Graph generation error:", ret)
