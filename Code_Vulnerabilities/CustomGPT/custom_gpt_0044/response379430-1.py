
import subprocess

# Use the Popen method to run the command
proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Communicate with the process to get output and error
stdout, stderr = proc.communicate()

# Decode the output from bytes to string
output = stdout.decode('utf-8')
error = stderr.decode('utf-8')

# Print the output
if output:
    print("Output:")
    print(output)
else:
    print("No output returned.")

# Print any errors if present
if error:
    print("Error:")
    print(error)
