
def _doPing(self, host):
    for x in range(self.probes):  # Use range for Python 3 compatibility
        ans, unans = commands.getstatusoutput(
            "ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host
        )
        print("Ping output:", unans)  # Debugging print
        if 'unreachable' in unans.lower():
            print("Host is unreachable")
            continue
        self.rrdList.append(unans)
    return self.rrdList
