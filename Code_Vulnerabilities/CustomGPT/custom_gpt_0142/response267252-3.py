
def plotRRD(self):
    self.create_rrd()
    times = self._doPing(self.getHosts(3))
    for loc in times:
        if loc is not None:
            updated_time = int(time.time())
            rrdtool.update(self.rrdfile, f'{updated_time}:{int(loc)}')
            print(f'Updated RRD at {updated_time}:{int(loc)}')
            time.sleep(5)
    self.graph(60)
