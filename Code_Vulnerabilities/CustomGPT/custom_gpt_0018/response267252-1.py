
def _doPing(self, host):
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        if ans == 0:
            print(f"Probe {x}: Successful ping to {host}. RTT: {unans}")
            self.rrdList.append(unans)  # Append successful RTT
        else:
            print(f"Probe {x}: Failed to ping {host}.")
            self.rrdList.append(0)  # Append 0 if no response
    return self.rrdList

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for loc in times:
        if loc > 0:  # Only update the RRD if we received a valid RTT
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print('%d:%d' % (int(time.time()), int(float(loc))))
            time.sleep(5)
        else:
            print("No valid RTT to update.")
    self.graph(60)
