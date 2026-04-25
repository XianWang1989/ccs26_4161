
def plotRRD(self):
    self.create_rrd()
    times = self._doPing(self.getHosts(3))
    for loc in times:
        if loc > 0:  # Only update if we have a valid response time
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(loc)))
            print('%d:%d' % (int(time.time()), int(loc)))
            time.sleep(5)
    self.graph()
