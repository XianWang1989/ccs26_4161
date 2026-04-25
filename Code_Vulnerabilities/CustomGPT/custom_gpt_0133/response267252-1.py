
def create_rrd(self):
    # Create the RRD file if it doesn't exist
    if not os.path.exists(self.rrdfile):
        ret = rrdtool.create(
            self.rrdfile,
            "--step", str(self.interval),
            "DS:packets:COUNTER:600:U:U",
            "RRA:AVERAGE:0.5:1:288",
            "RRA:AVERAGE:0.5:1:336"
        )
        if ret:
            print("Error creating RRD file:", rrdtool.error())
    else:
        print("RRD file already exists.")

def _doPing(self, host):
    for x in range(self.probes):  # Use range for Python 3 compatibility
        ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
        print(f'Probe {x}: {ans}, Unanswered: {unans}')
        if ans != 0:  # Check if the ping command was successful
            print("Ping failed or no response.")
            self.rrdList.append(0)  # Append 0 packets if ping failed
        else:
            self.rrdList.append(float(unans) if unans else 0)

def plotRRD(self):
    self.create_rrd()

    times = self._doPing(self.getHosts(3))
    curr_time = int(time.time())
    for loc in times:
        rrdtool.update(self.rrdfile, f'{curr_time}:{loc}')
        print(f'Data updated: {curr_time}:{loc}')
        curr_time += self.interval  # To represent the passage of time
        time.sleep(5)

    self.graph(60)
