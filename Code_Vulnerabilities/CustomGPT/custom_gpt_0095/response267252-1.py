
def _doPing(self, host):
    for x in range(self.probes):  # Changed from xrange to range for Python 3
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt" % host)
        if ans == 0:  # If ping was successful
            rtt = unans.split('/')[4]  # Extract the RTT value
            self.rrdList.append(float(rtt))  # Store RTT as float
        else:
            print(f"Ping to {host} failed.")
            self.rrdList.append(0)  # Handle failure case
    return self.rrdList

def graph(self, mins):
    start_time = int(time.time()) - mins * 60  # Calculate start time
    ret = rrdtool.graph("%s.png" % self.rrdfile,
                        "--start", str(start_time),  # Use calculated start time
                        "--end", str(int(time.time())),
                        "--step", "300",
                        "--vertical-label=Bytes/s",
                        "DEF:inoctets=%s:packets:AVERAGE" % self.rrdfile,
                        "AREA:inoctets#7113D6:In traffic",
                        "COMMENT:\\n",
                        "GPRINT:inoctets:AVERAGE:Avg In traffic\: %6.2lf",
                        "COMMENT:  ",
                        "GPRINT:inoctets:MAX:Max In traffic\: %6.2lf")
