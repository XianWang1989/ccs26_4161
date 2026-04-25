
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for time_sample in times:
        if time_sample:  # Only update if there is a valid time sample
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(time_sample))))
            print('%d:%d' % (int(time.time()), int(float(time_sample))))
        else:
            print("No valid ping response, skipping update.")
        time.sleep(5)
    self.graph(60)
