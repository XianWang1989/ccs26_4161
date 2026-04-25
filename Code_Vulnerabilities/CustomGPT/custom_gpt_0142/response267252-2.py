
def _doPing(self, host):
    self.rrdList = []  # Reset list for every call
    for x in range(self.probes):  # Use `range` instead of `xrange` for Python 3 compatibility
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        if ans != 0:  # This means ping failed
            print(f"Ping failed for {host}: {unans}")
            self.rrdList.append(0)  # Append zero or some default value
        else:
            self.rrdList.append(float(unans))
    return self.rrdList
