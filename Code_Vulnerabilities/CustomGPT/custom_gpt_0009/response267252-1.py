
def _doPing(self, host):
    for x in range(self.probes):  # Use range for Python 3
        ans, output = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        if ans != 0:  # Check if ping was successful
            print(f"Ping failed for {host}")
            self.rrdList.append(0)  # Append zero or some indicator for failure
        else:
            print(x)
            self.rrdList.append(float(output))  # Store latency value
    return self.rrdList

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for x in range(len(times)):
        loc = times.pop(0)
        # Don't try to update with a zero or invalid value
        if loc > 0:  
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(loc)))
            print('%d:%d' % (int(time.time()), int(loc)))
        else:
            print("No valid ping response to log.")
        time.sleep(5)
    self.graph(60)
