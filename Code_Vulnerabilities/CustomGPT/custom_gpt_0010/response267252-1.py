
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))

    for x in range(len(times)):
        loc = times.pop(0)

        if loc.isdigit():
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print('%d:%d' % (int(time.time()), int(float(loc))))
        else:
            print(f"Invalid ping response: {loc}")

        time.sleep(5)

    self.graph(60)

def graph(self, mins):
    start_time = int(time.time()) - mins * 60
    ret = rrdtool.graph("%s.png" % self.rrdfile,
                        "--start", str(start_time),
                        "--end", str(int(time.time())),
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
        print("Graph created successfully.")
    else:
        print("Error creating graph.")
