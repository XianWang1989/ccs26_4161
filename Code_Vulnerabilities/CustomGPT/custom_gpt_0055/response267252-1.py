
def _doPing(self, host):
    for x in range(self.probes):
        # Run the ping command and capture the output
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        # Ensure that the output is valid
        if ans == 0:
            self.rrdList.append(float(unans))
        else:
            print("Ping failed or returned no result for host:", host)

def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)
    for loc in times:
        update_status = rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(loc)))
        if update_status is not None:
            print('Update failed:', update_status)
        time.sleep(5)
    self.graph(60)
