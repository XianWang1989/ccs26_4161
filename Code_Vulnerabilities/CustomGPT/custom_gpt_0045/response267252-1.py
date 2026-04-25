
def _doPing(self, host):
    for x in range(self.probes):  # Updated for Python 3
        ans, unans = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        if ans == 0:  # Check if ping was successful
            print(f"Probe {x} successful for {host}: RTT {unans}")
            self.rrdList.append(unans)
        else:
            print(f"Probe {x} failed for {host}")
            self.rrdList.append(0)  # Append 0 or some default value
    return self.rrdList 
