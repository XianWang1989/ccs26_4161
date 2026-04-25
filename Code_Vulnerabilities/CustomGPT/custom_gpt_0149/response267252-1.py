
def _doPing(self, host):
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        ans, unans = commands.getstatusoutput(
            "ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host
        )
        if ans == 0:  # Check if ping was successful
            self.rrdList.append(float(unans))
        else:
            self.rrdList.append(0)  # Append 0 for failed pings
    return self.rrdList 

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for loc in times:
        timestamp = int(time.time())
        rrdtool.update(self.rrdfile, '%d:%d' % (timestamp, int(loc)))
        print('%d:%d' % (timestamp, int(loc)))
        time.sleep(5)
    self.graph(60)
