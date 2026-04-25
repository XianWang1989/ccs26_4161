
def _doPing(self, host):
    self.rrdList = []  # Clear previous results
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)

        # Check if the output is non-empty and numeric
        if ans == 0 and unans:
            try:
                self.rrdList.append(float(unans))  # Store RTT value as float
            except ValueError:
                print("Non-numeric RTT value received.")
                self.rrdList.append(0)
        else:
            print(f"Ping failed for {host}.")
            self.rrdList.append(0)  # Append a default value on failure

    return self.rrdList

def graph(self, mins):
    ret = rrdtool.graph("%s.png" % self.rrdfile, 
                        "--start", "-%d" % (mins * 60),
                        "--step", "%d" % self.interval,
                        "--vertical-label=ms",
                        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                        "LINE1:inoctets#FF0000:RTT",
                        "GPRINT:inoctets:LAST:Last RTT\: %6.2lf ms",
                        "GPRINT:inoctets:AVERAGE:Avg RTT\: %6.2lf ms",
                        "GPRINT:inoctets:MAX:Max RTT\: %6.2lf ms",
                        "COMMENT:\\n")
