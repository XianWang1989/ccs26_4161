
def plotRRD(self):
    if not os.path.exists(self.rrdfile):
        self.create_rrd(self.interval)

    times = self._doPing(self.getHosts(3))
    for loc in times:
        # Check if loc is a numeric value before updating
        try:
            loc_value = int(float(loc))
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), loc_value))
            print('%d:%d' % (int(time.time()), loc_value))
        except ValueError:
            print(f"Invalid location value: {loc}")
        time.sleep(5)

    self.graph(60)
