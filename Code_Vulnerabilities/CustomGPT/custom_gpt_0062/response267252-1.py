
def plotRRD(self):
    self.create_rrd(self.interval)

    try:
        host = self.getHosts(3)
        print(f"Pinging host: {host}")
        times = self._doPing(host)

        for x in range(len(times)):
            loc = times.pop(0)
            if loc and loc.strip():  # Check if loc has a valid value
                rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
                print(f'Updated RRD with: {int(time.time())}:{int(float(loc))}')
            else:
                print("Ping failed or returned an invalid response.")
            time.sleep(5)

        self.graph(60)
    except Exception as e:
        print(f"An error occurred: {e}")
