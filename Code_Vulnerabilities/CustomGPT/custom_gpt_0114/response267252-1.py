
def _doPing(self, host):
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
        if ans == 0:  # Check if the ping command succeeded
            self.rrdList.append(float(unans))  # Append the RTT as float
        else:
            self.rrdList.append(0)  # Append 0 if ping failed
    return self.rrdList

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for loc in times:  # Directly iterate over times
        current_time = int(time.time())
        rrdtool.update(self.rrdfile, f'{current_time}:{int(loc)}')
        print(f'{current_time}:{int(loc)}')
        time.sleep(5)
    self.graph(60)

def graph(self, mins):
    ret = rrdtool.graph(f"{self.rrdfile}.png", "--start", "-1", "--end", "+1", "--step", "300",
                        "--vertical-label=ms",
                        "DEF:packets={}:packets:AVERAGE".format(self.rrdfile),
                        "AREA:packets#7113D6:In traffic",
                        "COMMENT:\\n",
                        "GPRINT:packets:AVERAGE:Avg Ping Time: %6.2lf ms",
                        "GPRINT:packets:MAX:Max Ping Time: %6.2lf ms")
