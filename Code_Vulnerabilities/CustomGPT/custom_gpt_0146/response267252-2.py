
def _doPing(self, host):
    for x in range(0, self.probes):
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s| grep rtt| awk -F '/' '{ print $5 }'" % host)
        print("Ping result:", unans)  # Check what ping returns
        if ans != 0 or unans.strip() == "":
            self.rrdList.append(0)  # Append 0 or a designated value when ping fails
        else:
            self.rrdList.append(unans)
    return self.rrdList
