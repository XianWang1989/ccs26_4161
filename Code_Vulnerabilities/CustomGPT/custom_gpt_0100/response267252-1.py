
def _doPing(self, host):
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        if ans == 0:
            print(f"Ping response: {unans}")
            self.rrdList.append(unans)
        else:
            print(f"Ping failed for {host}: {unans}")
    return self.rrdList 

def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)

    times = self._doPing(host)
    for loc in times:
        timestamp = int(time.time())
        if loc:  # Ensure loc is valid
            rrdtool.update(self.rrdfile, '%d:%d' % (timestamp, int(float(loc))))
            print('%d:%d' % (timestamp, int(float(loc))))
        else:
            print("No valid RTT to update RRD.")
        time.sleep(5)
    self.graph(60)
