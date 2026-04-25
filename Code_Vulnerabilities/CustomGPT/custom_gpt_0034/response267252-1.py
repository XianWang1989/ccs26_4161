
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)

    for x in range(len(times)):
        loc = times.pop(0).strip()  # Clean the output
        if loc.isdigit():  # Ensure it's a valid integer
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            print(f'{int(time.time())}:{int(loc)}')
        else:
            print(f"Invalid ping response for {host}: {loc}")
        time.sleep(5)

    self.graph(60)

def graph(self, mins):
    ret = rrdtool.graph(f"{self.rrdfile}.png", 
                        "--start", "-1", "--end", "+1", "--step", "300",
                        "--vertical-label=Bytes/s",
                        f"DEF:inoctets={self.rrdfile}:packets:AVERAGE",
                        "AREA:inoctets#7113D6:In traffic",
                        "CDEF:inbits=inoctets,8,*",
                        "COMMENT:\\n",
                        "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                        "COMMENT:  ",
                        "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
    if ret:
        print(f"Graph generated with errors: {rrdtool.error()}")

