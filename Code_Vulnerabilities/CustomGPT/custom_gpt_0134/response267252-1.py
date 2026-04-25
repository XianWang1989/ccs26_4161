
import subprocess

def _doPing(self, host):
    for x in range(self.probes):  # Changed from xrange to range for Python 3
        cmd = ["ping", "-c", "3", "-w", "6", host]
        try:
            output = subprocess.check_output(cmd).decode()
            rtt_line = [line for line in output.split("\n") if "rtt" in line]
            if rtt_line:
                rtt_values = rtt_line[0].split("=")[-1].split("/")[4].strip()
                self.rrdList.append(rtt_values)
            else:
                self.rrdList.append('0')  # Handle no response case
        except subprocess.CalledProcessError:
            print(f"Ping failed for {host}")
            self.rrdList.append('0')
    return self.rrdList
