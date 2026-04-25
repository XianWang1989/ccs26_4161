
import subprocess

# Run the 'bjobs' command
result = subprocess.run(['bjobs'], capture_output=True, text=True)

# Capture the standard output
output = result.stdout
error = result.stderr

# Check if the command was successful
if result.returncode == 0:
    print("Command output:")
    print(output)
else:
    print("Error occurred:")
    print(error)
