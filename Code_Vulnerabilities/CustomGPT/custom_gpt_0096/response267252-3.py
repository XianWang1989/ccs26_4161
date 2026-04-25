
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for loc in times:
        if loc.strip():  # Ensure loc is not empty
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print('Updated RRD with:', '%d:%d' % (int(time.time()), int(float(loc))))
        else:
            print("No valid data to update.")
        time.sleep(5)
    self.graph(60)
