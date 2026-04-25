
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)

    for x in range(len(times)):
        loc = times.pop(0)
        if loc:  # Check if loc is not empty
            status = rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            if status:
                print(f"Update failed: {status}")
            else:
                print('%d:%d' % (int(time.time()), int(float(loc))))
                time.sleep(5)

    self.graph(60)
