
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for loc in times:
        if loc is not None:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
        time.sleep(5)
    self.graph(60)
