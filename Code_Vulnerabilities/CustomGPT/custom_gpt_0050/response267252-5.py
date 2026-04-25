
def create_rrd(self, interval):
    ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                         "DS:packets:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:1:288",
                         "RRA:AVERAGE:0.5:1:336")
    if ret:
        print("Error creating RRD file:", ret)

def _doPing(self, host):
    results = []
    for _ in range(self.probes):
        status, output = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt" % host)
        if status == 0:
            rtt = output.split('/')
            results.append(float(rtt[4]))  # average RTT
        else:
            print("Ping failed for host:", host)
            results.append(0)
    return results

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for loc in times:
        if loc:
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(loc)}')
            print(f'Updated RRD with: {int(time.time())}:{int(loc)}')
        else:
            print("No valid data to update")
        time.sleep(5)
    self.graph(60)
