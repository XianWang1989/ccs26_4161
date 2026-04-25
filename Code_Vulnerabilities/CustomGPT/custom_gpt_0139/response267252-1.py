
def _doPing(self, host):
    for x in range(self.probes):  # Use range() for Python 3 compatibility
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        if ans != 0:  
            print(f"Ping failed for {host}: {unans}")
            self.rrdList.append(0)  # Add a default value in case of failure
        else:
            print(x)
            self.rrdList.append(unans)
        time.sleep(1)  # Add sleep if you want to space out the pings
    return self.rrdList
