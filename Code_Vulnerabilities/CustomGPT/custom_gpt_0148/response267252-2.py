
import subprocess

def _doPing(self, host):
    for x in range(self.probes):
        try:
            result = subprocess.run(
                ["ping", "-c", "3", "-w", "6", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output = result.stdout
            rtt = self.extract_rtt(output)
            self.rrdList.append(rtt)
        except Exception as e:
            print(f"Error pinging {host}: {e}")
    return self.rrdList

def extract_rtt(self, output):
    for line in output.splitlines():
        if 'rtt' in line:
            return float(line.split('/')[4])
    return None
