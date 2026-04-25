
def _doPing(self, host):
    for x in range(self.probes):  # Changed to Python 3 syntax
        ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host}| grep rtt| awk -F '/' '{ print $5 }'")
        print(f"Ping attempt {x}: {ans}, response: {unans}")  # Debugging output
        if ans == 0:  # Command succeeded
            self.rrdList.append(unans)
        else:
            print(f"Failed to ping {host}: {ans}")

def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    print(f"Pinging host: {host}")
    times = self._doPing(host)
    print(f"Ping results: {times}")  # Print collected ping results
    for loc in times:
        if loc:
            try:
                rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(loc))}')
                print(f'Updated RRD: {int(time.time())}:{int(float(loc))}')
            except Exception as e:
                print(f"Error updating RRD: {e}")
        time.sleep(5)
    self.graph(60)
