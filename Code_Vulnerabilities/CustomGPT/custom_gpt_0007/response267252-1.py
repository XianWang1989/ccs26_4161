
def _doPing(self, host):
    for x in range(0, self.probes):
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)

        print(f'Ping attempt {x}: {unans}')  # Debugging output
        if ans == 0:
            self.rrdList.append(unans)  # Append RTT return value
        else:
            self.rrdList.append("0")  # Could not ping, append default value
        time.sleep(1)  # Optional: reduce frequency of pinging
    return self.rrdList

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))

    for x in range(len(times)):
        loc = times.pop(0)
        try:
            # Ensure loc is a number before updating
            value = int(float(loc))
        except ValueError:
            print(f"Error processing value '{loc}' as integer. Skipping update.")
            continue

        rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), value))
        print(f'Updated RRD with timestamp {int(time.time())} and value {value}')
        time.sleep(5)

    self.graph(60)

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
