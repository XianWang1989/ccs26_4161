
import subprocess

# Run the bjobs command
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capture the output and error
output = result.stdout
error = result.stderr

# Print the output or error
if output:
    print("Output:", output)
if error:
    print("Error:", error)
