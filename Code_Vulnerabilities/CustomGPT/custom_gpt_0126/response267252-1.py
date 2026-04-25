
def create_rrd(self):
    try:
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:GAUGE:600:0:U",
                             "RRA:AVERAGE:0.5:1:288")
        if ret:
            print(rrdtool.error())
    except Exception as e:
        print(f"Error creating RRD: {e}")

def _doPing(self, host):
    results = []
    for _ in range(self.probes):
        cmd = f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'"
        ans, unans = commands.getstatusoutput(cmd)
        if ans == 0:
            results.append(unans)
        else:
            results.append("0")  # Add a default value for failed pings
    return results

def plotRRD(self):
    self.create_rrd()
    times = self._doPing(self.getHosts(3))

    for loc in times:
        try:
            rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(float(loc))}")
            time.sleep(5)
        except Exception as e:
            print(f"Error updating RRD: {e}")

    self.graph(60)
