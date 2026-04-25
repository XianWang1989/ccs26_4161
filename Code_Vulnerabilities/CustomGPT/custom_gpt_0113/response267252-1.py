
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))

    for loc in times:
        if loc and loc.isnumeric():  # Ensure loc is a numeric value
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            print(f'{int(time.time())}:{int(loc)}')
            time.sleep(5)

    self.graph(60)

def graph(self, mins):
    rrdtool.graph(f"{self.rrdfile}.png",
                  "--start", str(-mins * 60),
                  "--step", "300",
                  "--vertical-label=Bytes/s",
                  f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                  "AREA:inoctets#7113D6:In traffic",
                  "CDEF:inbits=inoctets,8,*",
                  "COMMENT:\\n",
                  "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                  "COMMENT:  ",
                  "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
