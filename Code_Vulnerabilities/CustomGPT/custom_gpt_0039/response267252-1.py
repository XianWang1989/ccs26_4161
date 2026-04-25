
def _doPing(self, host):
    for x in range(self.probes):  # Use 'range' for Python 3 compatibility
        ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
        if ans != 0:  # Check if ping was successful
            print(f"Ping failed: {unans}")
            self.rrdList.append(0)  # Append 0 or some error indicator
        else:
            self.rrdList.append(float(unans.strip()))  # Ensure floats are appended
    return self.rrdList

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for timestamp in range(len(times)):
        loc = times[timestamp]
        if loc > 0:  # Proceed if loc is valid
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            print(f'{int(time.time())}:{int(loc)}')
        else:
            print("No valid data to update.")
        time.sleep(5)
    self.graph(60)  # Update graph after all data is collected
