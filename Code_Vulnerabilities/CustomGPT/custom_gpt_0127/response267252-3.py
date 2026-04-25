
import subprocess

def _doPing(self, host):
    for x in range(0, self.probes):
        try:
            result = subprocess.check_output(
                ["ping", "-c", "3", "-w", "6", host],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            rtt = result.split('rtt')[1].strip().split('/')[4]
            self.rrdList.append(rtt)
        except subprocess.CalledProcessError as e:
            print(f"Ping failed: {e.output}")
