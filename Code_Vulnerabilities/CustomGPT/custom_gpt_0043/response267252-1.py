
def create_rrd(self, interval):
    ret = rrdtool.create("%s" % self.rrdfile, "--step", "%s" % self.interval,
                         "DS:packets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:1:288",
                         "RRA:AVERAGE:0.5:1:336")
    if ret:
        print("Error creating RRD:", ret)

def _doPing(self, host):
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        print(f"Ping {x}: ", ans, unans) # Debug output
        if unans:
            self.rrdList.append(unans)
        else:
            print(f"No response for {host}")

# Ensure there is enough data for the graph to plot
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))

    if not times:
        print("No valid response times to log.")
        return

    for x in range(len(times)):
        loc = times.pop(0)
        try:
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print('%d:%d' % (int(time.time()), int(float(loc))))
            time.sleep(5)
        except Exception as e:
            print("Error updating RRD:", e)

    self.graph(60)

# Adjust the graphing to include checks on data
def graph(self, mins):
    ret = rrdtool.graph("%s.png" % self.rrdfile, "--start", "-1", "--end", "+1", "--step", "300",
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                        "AREA:inoctets#7113D6:In traffic",
                        "CDEF:inbits=inoctets,8,*",
                        "COMMENT:\\n",
                        "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                        "COMMENT:  ",
                        "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")

    if ret:
        print("Error creating graph:", ret)
