
def _doPing(self, host):
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
        if ans == 0:
            self.rrdList.append(float(unans))  # Append valid RTT value
        else:
            self.rrdList.append(0)  # Append 0 if host unreachable
    return self.rrdList 

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for x in range(len(times)):
        loc = times[x]
        rrdtool.update(self.rrdfile, f'{int(time.time())}:{loc}')
        print(f'{int(time.time())}:{loc}')
        time.sleep(5)
    self.graph(60)
