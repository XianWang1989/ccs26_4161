
def _doPing(self, host):
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        ans, unans = commands.getstatusoutput(
            "ping -c 3 -w 6 %s | grep rtt | awk -F '/' '{ print $5 }'" % host
        )
        if ans == 0 and unans:  # Check if the ping was successful
            self.rrdList.append(unans)
        else:
            print("Ping failed for host: %s" % host)
            self.rrdList.append(0)  # Append 0 if ping fails
    return self.rrdList 

# Ensure the RRD is created only once
if __name__ == "__main__":
    ping = rrdPing()
    if not os.path.exists(ping.rrdfile):  # Check if the file exists
        ping.create_rrd(ping.interval)    # Create RRD if it doesn't exist
    ping.plotRRD()
    info = rrdtool.info(ping.rrdfile)
    print(info['last_update'])
