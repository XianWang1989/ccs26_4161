
def _doPing(self, host):
    results = []
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        print(f"Ping output for {host}: {unans}")  # Print the output of ping
        if ans == 0:  # Check if the ping command was successful
            results.append(unans)
        else:
            results.append(0)  # If failed, append 0 or handle the error
    return results
