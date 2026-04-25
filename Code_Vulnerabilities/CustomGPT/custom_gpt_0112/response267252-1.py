
def _doPing(self, host):
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        print("Probe #%d: %s" % (x+1, unans))
        if ans == 0:  # Successful ping
            self.rrdList.append(unans)
        else:
            print("Ping failed for %s" % host)

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for time_response in times:
        try:
            current_time = int(time.time())
            response_time = int(float(time_response))
            rrdtool.update(self.rrdfile, '%d:%d' % (current_time, response_time))
            print('Updated RRD with %d:%d' % (current_time, response_time))
            time.sleep(5)
        except ValueError:
            print("Invalid response: %s" % time_response)
    self.graph(60)

def graph(self, mins):
    ret = rrdtool.graph("%s.png" % self.rrdfile,
                        "--start", "-%s" % mins * 60,
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                        "AREA:inoctets#7113D6:In traffic",
                        "CDEF:inbits=inoctets,8,*",
                        "COMMENT:\\n",
                        "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf \\r",
                        "GPRINT:inbits:MAX:Max In traffic\: %6.2lf")
    print("Graph created: %s.png" % self.rrdfile)
