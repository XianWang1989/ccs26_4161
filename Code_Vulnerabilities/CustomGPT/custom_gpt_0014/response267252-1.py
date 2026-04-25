
import subprocess

def _doPing(self, host):
    for x in range(self.probes):  # Use range instead of xrange for Python 3
        try:
            output = subprocess.check_output(f"ping -c 3 -w 6 {host}", shell=True)
            rtt = output.decode().splitlines()[-1].split('/')[4]
            self.rrdList.append(rtt)
        except subprocess.CalledProcessError as e:
            print(f"Error pinging {host}: {e}")
            self.rrdList.append(0)  # Append a default value on error
    return self.rrdList 

def plotRRD(self):
    self.create_rrd(self.interval)
    times = self._doPing(self.getHosts(3))
    for rtt in times:
        if rtt:  # Only update if RTT is valid
            rtt_float = float(rtt)
            rrdtool.update(self.rrdfile, f'{int(time.time())}:{int(rtt_float)}')
            print(f'{int(time.time())}:{int(rtt_float)}')
            time.sleep(5)
    self.graph(60)
