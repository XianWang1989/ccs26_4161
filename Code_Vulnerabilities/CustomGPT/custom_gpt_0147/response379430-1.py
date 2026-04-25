
import subprocess

# Running the 'bjobs' command and capturing the output
result = subprocess.run(['bjobs'], capture_output=True, text=True)

# Checking if the command was successful
if result.returncode == 0:
    output = result.stdout  # Capture the output
    print("Output from bjobs:")
    print(output)
else:
    print("Error occurred:")
    print(result.stderr)  # Print any error if occurred
