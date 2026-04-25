
def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))

    for x in range(len(times)):
        loc = times.pop(0)

        # Debugging the location variable
        if loc and loc.isdigit():  # Ensure it's a valid number
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
            print('%d:%d' % (int(time.time()), int(float(loc))))
        else:
            print(f"Invalid location value: {loc}")

        time.sleep(5)

    # Adjust the graph period as needed
    self.graph(60)
