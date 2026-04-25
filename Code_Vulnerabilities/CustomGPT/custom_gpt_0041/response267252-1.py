
def _doPing(self, host):
    results = []
    for x in range(self.probes):  # Use range for Python 3 compatibility
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        print(f"Probe {x}: Status = {ans}, Output = {unans}")  # Debug info
        if unans:  # Check if there was a valid response
            results.append(float(unans))
        else:
            print("No response from host")
    return results

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for loc in times:
        if loc:  # Ensure loc is not empty or invalid
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(loc)))
            print('%d:%d' % (int(time.time()), int(loc)))
            time.sleep(5)  # Adjust based on your probing needs
    self.graph(60)
