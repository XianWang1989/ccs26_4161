
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)

    for x in range(len(times)):
        loc = times[x]
        if loc and loc.strip():  # Check if loc is valid
            try:
                rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            except Exception as e:
                print(f"Error updating RRD: {e}")
                continue
            print('%d:%d' % (int(time.time()), int(float(loc))))
        else:
            print("Ping failed or returned no value.")
        time.sleep(5)

    self.graph(60)

def graph(self, mins):
    start_time = "-%d" % (mins * 60)  # Adjust starting time to the correct format
    ret = rrdtool.graph("%s.png" % self.rrdfile,
                        "--start", start_time,
                        "--step", "300",
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                        "AREA:inoctets#7113D6:In traffic",
                        "CDEF:inbits=inoctets,8,*",
                        "COMMENT:\\n",
                        "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                        "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
    if ret:
        print(f"Graph created: {self.rrdfile}.png")
    else:
        print("Graphing failed.")
