
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for loc in times:
        if loc:  # Check that loc is not empty
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            print(f'Updated RRD with: {int(time.time())}:{int(loc)}')
        else:
            print("No valid data to update")
        time.sleep(5)
    self.graph(60)
