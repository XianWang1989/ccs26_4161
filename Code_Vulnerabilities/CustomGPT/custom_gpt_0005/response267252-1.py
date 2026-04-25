
def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    times = self._doPing(host)

    for x in range(len(times)):
        loc = times[x]
        try:
            if loc:  # Check if location is valid
                rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), int(float(loc))))
                print('%d:%d' % (int(time.time()), int(float(loc))))
            else:
                print(f"No valid response from {host}")
        except Exception as e:
            print(f"Error updating RRD: {e}")
        time.sleep(5)

    # Generating the graph
    try:
        self.graph(60)
    except Exception as e:
        print(f"Error generating graph: {e}")
