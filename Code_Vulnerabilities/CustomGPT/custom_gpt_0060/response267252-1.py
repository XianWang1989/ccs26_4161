
def plotRRD(self):
    self.create_rrd(self.interval)

    # Ensure we get a valid host
    host = self.getHosts(3)

    # Verify Host validity
    if not host:
        print("No host found.")
        return

    # Ping and process results
    times = self._doPing(host)

    if not times:
        print("No responses from ping.")
        return

    for ping_response in times:
        if ping_response:  # Ensure response is valid
            ping_time = int(time.time())
            rrdtool.update(self.rrdfile, '%d:%d' % (ping_time, int(float(ping_response))))
            print('%d:%d' % (ping_time, int(float(ping_response))))
            time.sleep(5)

    # Graph only if there's at least one successful update
    if times:
        self.graph(60)
    else:
        print("No data to graph.")
