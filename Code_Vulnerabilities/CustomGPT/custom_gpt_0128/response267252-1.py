
def _doPing(self, host):
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        rtt_value = unans.strip()
        if not rtt_value:
            print(f"Ping failed for {host}")
            continue
        self.rrdList.append(rtt_value)
    return self.rrdList 

def plotRRD(self):
    self.create_rrd(self.interval)
    host = self.getHosts(3)
    print(f"Pinging host: {host}")

    times = self._doPing(host)
    for loc in times:
        if loc:  # ensure loc is valid
            rrdtool.update(self.rrdfile, f"{int(time.time())}:{int(float(loc))}")
            print(f"{int(time.time())}:{int(float(loc))}")
        time.sleep(5)
    self.graph(60)
