
def graph(self, mins):
    ret = rrdtool.graph("%s.png" % self.rrdfile,
                        "--start", "-%d" % mins,  # Use negative mins for starting time
                        "--step", "300",
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                        "AREA:inoctets#7113D6:In traffic",
                        "CDEF:inbits=inoctets,8,*",
                        "COMMENT:\\n",
                        "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                        "COMMENT:  ",
                        "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
    if ret:
        print("Graphing Error:", ret)  # Show any error that might occur during the graphing process
