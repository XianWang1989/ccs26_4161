
def _doPing(self, host):
    for x in range(self.probes):
        ans, unans = commands.getstatusoutput(f"ping -c 1 -w 1 {host}| grep rtt | awk -F '/' '{{ print $5 }}'")
        if ans == 0:  # Check if ping was successful
            print(f"Ping successful: {unans} ms")
            self.rrdList.append(unans)
        else:
            print("Ping failed.")
            self.rrdList.append(0)  # Add zero or a default value in case of failure

def graph(self, mins):
    # Adjust graph parameters and labels if necessary
    ret = rrdtool.graph(f"{self.rrdfile}.png", 
                        "--start", f"-{mins}m", 
                        "--vertical-label=ms",
                        "DEF:avg_rtt=%s:packets:AVERAGE" % self.rrdfile,
                        "LINE2:avg_rtt#FF0000:Avg RTT",
                        "COMMENT:\\n",
                        "GPRINT:avg_rtt:AVERAGE:Average RTT\: %6.2lf ms\\n")
