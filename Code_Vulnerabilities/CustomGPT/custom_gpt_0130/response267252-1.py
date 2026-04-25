
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)

    for loc in times:
        if loc:  # Check if loc is valid
            try:
                loc_value = int(float(loc))
                rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), loc_value))
                print('%d:%d' % (int(time.time()), loc_value))
                time.sleep(5)
            except ValueError:
                print(f"Invalid ping result: {loc}")
        else:
            print("No response for ping.")

    self.graph(60)
