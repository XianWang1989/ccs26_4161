
def _doPing(self, host):
    for x in range(self.probes):  # Use range for Python 3 compatibility
        status, output = commands.getstatusoutput("ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host)
        print(f"Probe {x}: {status}")

        if status == 0 and output:  # Check for successful ping and non-empty output
            self.rrdList.append(output)
        else:
            print(f"Ping failed for {host}: {output}")  # Debug output for failures
    return self.rrdList
