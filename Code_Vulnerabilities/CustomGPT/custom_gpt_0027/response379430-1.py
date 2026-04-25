
import subprocess

# Run the bjobs command
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capture the output and errors
output = result.stdout
error = result.stderr

# Print the output
if output:
    print("Output:")
    print(output)
if error:
    print("Error:")
    print(error)
