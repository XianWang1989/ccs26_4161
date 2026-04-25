
def graph(self, mins):
    try:
        rrdtool.graph("%s.png" % self.rrdfile,
                      "--start", "-%d" % mins,
                      "--step", str(self.interval),
                      "--vertical-label=Packets",
                      "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                      "AREA:inoctets#7113D6:In traffic",
                      "CDEF:inbits=inoctets,8,*",
                      "COMMENT:\\n",
                      "GPRINT:inbits:AVERAGE:Avg In traffic: %6.2lf",
                      "GPRINT:inbits:MAX:Max In traffic: %6.2lf")
    except Exception as e:
        print(f"Graphing failed: {e}")
