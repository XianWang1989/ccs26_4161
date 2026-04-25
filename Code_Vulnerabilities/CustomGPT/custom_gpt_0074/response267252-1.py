
def _doPing(self, host):
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        cmd = f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'"
        ans, unans = commands.getstatusoutput(cmd)
        print(f"Ping attempt {x + 1}: {unans}")  # Print output for debugging
        if not unans.isdigit():  # Check if the output is not a number
            print("Ping failed or returned invalid data.")
            continue  # Skip if there's an error
        self.rrdList.append(unans)
    return self.rrdList 
