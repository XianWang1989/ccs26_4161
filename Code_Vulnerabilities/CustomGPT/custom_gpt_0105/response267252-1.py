
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))

    for x in range(len(times)):
        loc = times.pop(0)
        if loc.isdigit():  # Check if the loc value is valid
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print('Updated RRD with: %d:%d' % (int(time.time()), int(float(loc))))
        else:
            print('Invalid ping response:', loc)
        time.sleep(5)

    # Generate the graph if there is enough data
    if len(times) > 0:
        self.graph(60)
    else:
        print('No data available for graphing!')
