
import subprocess

# Run the LSF command and capture output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get stdout and stderr
output = result.stdout
error = result.stderr

# Print the output
if output:
    print("Output:", output)
else:
    print("No output returned.")

# Print any errors
if error:
    print("Error:", error)
