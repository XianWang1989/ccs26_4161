
def create_rrd(self):
    try:
        ret = rrdtool.create(self.rrdfile, "--step", str(self.interval),
                             "DS:packets:COUNTER:600:U:U",
                             "RRA:AVERAGE:0.5:1:288",
                             "RRA:AVERAGE:0.5:1:336")
        if ret:
            print("Error creating RRD:", rrdtool.error())
    except Exception as e:
        print("Exception occurred:", e)

def _doPing(self, host):
    for _ in range(self.probes):
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        print("Ping response:", ans, unans)  # Debug output
        if unans:
            self.rrdList.append(unans)
    return self.rrdList 

def plotRRD(self):
    self.create_rrd()
    times = self._doPing(self.getHosts(3))
    for loc in times:
        try:
            loc_value = int(float(loc))
            rrdtool.update(self.rrdfile, '%d:%d' % (int(time.time()), loc_value))
            print('%d:%d' % (int(time.time()), loc_value))
            time.sleep(self.interval)  # Sleep for the interval duration
        except Exception as e:
            print("Error updating RRD:", e)
    self.graph(60)
