
def plotRRD(self):
    self.create_rrd()
    times = self._doPing(self.getHosts(3))

    for loc in times:
        timestamp = int(time.time())
        ret = rrdtool.update(self.rrdfile, '%d:%d' % (timestamp, int(float(loc))))

        if ret:
            print("Error updating RRD file:", ret)
        else:
            print('%d:%d' % (timestamp, int(float(loc))))
        time.sleep(5)

    self.graph(60)
