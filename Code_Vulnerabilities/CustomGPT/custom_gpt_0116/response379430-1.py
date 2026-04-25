
import subprocess

# Run the LSF command
proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Capture the output and errors
stdout, stderr = proc.communicate()

# Decode output from bytes to string
output = stdout.decode('utf-8')
error = stderr.decode('utf-8')

# Print the results
if output:
    print("Standard Output:\n", output)
if error:
    print("Error Output:\n", error)
