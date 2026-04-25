
def plotRRD(self):
    self.create_rrd(self.interval)  # Ensure rrd is created first
    times = self._doPing(self.getHosts(3))  # Gather ping results
    for loc in times:
        loc = loc.strip()  # Clean up the output
        if loc:  # Check if loc has a value
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print('%d:%d' % (int(time.time()), int(float(loc))))
            time.sleep(self.interval)  # Wait for the defined interval
    self.graph(60)

def graph(self, mins):
    ret = rrdtool.graph("%s.png" % self.rrdfile,
                        "--start", "-%dmin" % mins,  # Show last 'mins' minutes
                        "--step", str(self.interval),
                        "--vertical-label=Packets",
                        "DEF:packets=%s:packets:AVERAGE" % self.rrdfile,
                        "LINE1:packets#7113D6:Packets",
                        "COMMENT:\\n",
                        "GPRINT:packets:AVERAGE:Avg Packets\: %6.2lf",
                        "GPRINT:packets:MAX:Max Packets\: %6.2lf")
