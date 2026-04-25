
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the standard output and error
output = result.stdout
error = result.stderr

# Print the output
if output:
    print("Job Status:\n", output)
else:
    print("Error:\n", error)
