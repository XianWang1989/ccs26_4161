
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for x in range(len(times)):
        loc = times.pop(0)
        update_status = rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
        if update_status:
            print("Update Error:", update_status)
        print('%d:%d' % (int(time.time()), int(float(loc))))
        time.sleep(5)
    graph_status = self.graph(60)
    if graph_status:
        print("Graph Error:", graph_status)
