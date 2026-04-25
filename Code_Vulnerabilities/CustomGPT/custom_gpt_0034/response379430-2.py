
import subprocess

# Using subprocess.Popen()
proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, error = proc.communicate()

print("Output:\n", output)
print("Error:\n", error)
