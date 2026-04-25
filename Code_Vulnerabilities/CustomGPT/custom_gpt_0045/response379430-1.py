
import subprocess

# Use subprocess.run (available in Python 3.5 and later) to execute the command
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if there's an error with the command
if result.returncode != 0:
    print("Error executing bjobs:", result.stderr)
else:
    # Capture the output into a variable
    output = result.stdout
    print("Output from bjobs:\n", output)
