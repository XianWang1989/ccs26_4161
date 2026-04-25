
def _doPing(self, host):
    results = []
    for _ in range(self.probes):
        status, output = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt" % host)
        if status == 0:
            rtt = output.split('/')  # adjust as necessary
            results.append(float(rtt[4]))  # get the average RTT
        else:
            print("Ping failed for host:", host)
            results.append(0)  # or handle it accordingly
    return results
