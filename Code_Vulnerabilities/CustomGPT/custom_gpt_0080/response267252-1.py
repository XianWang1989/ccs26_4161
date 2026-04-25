
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)

    for loc in times:
        print(f"Ping result: {loc}")
        if loc.isdigit():  # Check if loc is valid
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print(f'Updated RRD with timestamp: {int(time.time())}, value: {int(float(loc))}')
        else:
            print(f"Invalid ping result: {loc}")

        time.sleep(5)

    self.graph(60)
