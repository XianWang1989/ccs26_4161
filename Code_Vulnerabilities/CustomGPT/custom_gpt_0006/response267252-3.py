
import subprocess
...
result = subprocess.Popen(["ping", "-c", "3", "-w", "6", host], stdout=subprocess.PIPE)
output, _ = result.communicate()
