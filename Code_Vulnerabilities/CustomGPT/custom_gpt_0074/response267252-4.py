
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))

    for loc in times:
        if loc is not None and loc.isdigit():  # Validate data
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(float(loc))}')
            print(f'Updated RRD with: {int(time.time())}:{int(float(loc))}')
            time.sleep(5)

    self.graph(60)
