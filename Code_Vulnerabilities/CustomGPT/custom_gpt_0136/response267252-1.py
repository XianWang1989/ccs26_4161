
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)

    for x in range(len(times)):
        loc = times.pop(0)

        # Check if we received a valid response
        if loc:
            try:
                # Log the current time and value being updated
                value = int(float(loc))
                rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), value))
                print(f'Updated {self.rrdfile} with timestamp {int(time.time())} and value {value}')
            except ValueError as e:
                print(f"Error updating RRD: {e}")
        else:
            print(f"No valid response for ping to {host}")

        time.sleep(5)

    self.graph(60)
