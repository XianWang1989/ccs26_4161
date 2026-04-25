
def _doPing(self, host):
    for x in range(self.probes):  # use range() for Python 3 compatibility
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        print(f"Ping attempt {x + 1}: {ans}, {unans}")  # Debugging output
        if ans == 0:  # Check if the ping command was successful
            self.rrdList.append(unans)
        else:
            self.rrdList.append('0')  # Append zero if ping fails
    return self.rrdList 

def graph(self, mins):
    ret = rrdtool.graph("%s.png" % self.rrdfile,
                         "--start", "-1",
                         "--end", "+1",
                         "--step", "300",
                         "--vertical-label=ms",  # Change to ms for RTT
                         "DEF:inrtt=%s:packets:AVERAGE" % self.rrdfile,
                         "AREA:inrtt#7113D6:RTT",
                         "CDEF:inbits=inrtt",
                         "COMMENT:\\n",
                         "GPRINT:inbits:AVERAGE:Avg RTT\: %6.2lf ms\\r",
                         "GPRINT:inbits:MAX:Max RTT\: %6.2lf ms",
                         "GPRINT:inbits:LAST:Last RTT\: %6.2lf ms")
