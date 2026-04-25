
def _doPing(self, host):
    for x in range(self.probes):  # Use range() in Python 3
        ans, unans = commands.getstatusoutput(
            "ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host
        )
        if ans == 0:  # Check if command succeeded
            print(f"Probe {x + 1}: {unans}")
            self.rrdList.append(unans)  # Drop the future probe decrement
        else:
            print(f"Ping to {host} failed: {unans}")
            self.rrdList.append(0)  # Append zero if ping fails

def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)
    for loc in times:
        try:
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print(f'Updated RRD at {int(time.time())}: {int(float(loc))}')
            time.sleep(5)
        except Exception as e:
            print(f'Failed to update RRD: {e}')
    self.graph(60)
