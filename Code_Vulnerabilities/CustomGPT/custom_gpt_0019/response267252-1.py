
import rrdtool
import time
import commands

class rrdPing(RRDplot):
    # ... [rest of your class definition remains unchanged]

    def _doPing(self, host):
        rtt_values = []
        for _ in range(self.probes):
            ans, unans = commands.getstatusoutput(f"ping -c 3 -w 6 {host} | grep rtt | awk -F '/' '{{ print $5 }}'")
            if ans == 0:  # Success
                rtt_values.append(float(unans))
            else:
                rtt_values.append(0)  # Fallback for no response
        return rtt_values 

    def plotRRD(self):
        self.create_rrd(self.interval)
        times = self._doPing(self.getHosts(3))

        for loc in times:
            timestamp = int(time.time())
            rrdtool.update(self.rrdfile, f'{timestamp}:{loc}')
            print(f'{timestamp}:{loc}')  # Log the update
            time.sleep(self.interval)  # Ensure proper interval

        self.graph(60)
