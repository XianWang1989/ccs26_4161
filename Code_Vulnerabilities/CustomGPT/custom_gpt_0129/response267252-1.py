
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)

    for response_time in times:
        if response_time:  # Ensure response_time is not empty
            try:
                # Parse the response time, ensuring we have a valid number
                loc = float(response_time)
                rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(loc)))
                print('%d:%d' % (int(time.time()), int(loc)))
                time.sleep(5)
            except ValueError as e:
                print(f"Failed to update RRD with value '{response_time}': {e}")

    self.graph(60)
