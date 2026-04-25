
def _doPing(self, host):
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        if ans == 0:  # Ping was successful
            self.rrdList.append(unans)
        else:
            print("Ping failed:", unans)
    return self.rrdList
