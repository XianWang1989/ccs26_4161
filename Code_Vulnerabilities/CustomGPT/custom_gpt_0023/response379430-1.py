
import subprocess

# Use subprocess.run to execute the command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Capture the output into a variable
    output = result.stdout
    print(output)
else:
    # Handle the error if the command fails
    print("Error:", result.stderr)
