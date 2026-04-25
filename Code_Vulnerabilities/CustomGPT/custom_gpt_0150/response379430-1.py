
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the output and error (if any)
output = result.stdout
error = result.stderr

# Print the output
if output:
    print("Output:\n", output)
if error:
    print("Error:\n", error)
