
def _doPing(self, host):
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
        print(f"Probe {x}: {ans}, {unans}")  # Log outputs for debugging
        if ans == 0:  # Check if ping was successful
            self.rrdList.append(unans)
        else:
            print(f"Ping failed for {host}")
    return self.rrdList 

def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)
    for loc in times:
        if loc:  # Only update RRD if loc is not empty
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(loc))}')
            print(f'Updated RRD: {int(time.time())}:{int(float(loc))}')
            time.sleep(5)
    self.graph(60)
