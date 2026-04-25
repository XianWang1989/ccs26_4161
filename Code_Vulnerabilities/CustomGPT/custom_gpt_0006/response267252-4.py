
import subprocess

def _doPing(self, host):
    for x in range(self.probes):
        result = subprocess.Popen(["ping", "-c", "3", "-w", "6", host], stdout=subprocess.PIPE)
        output, _ = result.communicate()
        try:
            unans = output.decode().splitlines()[-1].split('/')[4]
        except IndexError:
            unans = '0'  # Default value if parsing fails
        self.rrdList.append(unans)
        print(f"Probe {x}: {unans}")
    return self.rrdList 
