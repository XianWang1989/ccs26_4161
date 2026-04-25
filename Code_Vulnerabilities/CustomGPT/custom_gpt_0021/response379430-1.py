
import subprocess

# Run the 'bjobs' command
proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Capture the output and error (if any)
stdout, stderr = proc.communicate()

# Decode the output from bytes to string, if necessary
output = stdout.decode('utf-8').strip()

# Check if there was an error
if proc.returncode != 0:
    print("Error:", stderr.decode('utf-8'))
else:
    print("Output:", output)
