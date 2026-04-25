
def _doPing(self, host):
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput(
            "ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host
        )
        if unans:
            self.rrdList.append(float(unans))
        else:
            self.rrdList.append(0)  # Handle failure
