
import subprocess

# Run the bjobs command
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capture the standard output and error
output = result.stdout
error = result.stderr

# Print the output
if result.returncode == 0:
    print("Output:\n", output)
else:
    print("Error:\n", error)
