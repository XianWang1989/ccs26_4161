
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))

    for x in range(len(times)):
        loc = times.pop(0)
        if loc:  # Ensure loc is not empty
            try:
                rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
                print('%d:%d' % (int(time.time()), int(float(loc))))
            except Exception as e:
                print("Error updating RRD:", str(e))
        time.sleep(5)

    # Generate the graph
    self.graph(60)
