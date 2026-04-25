
import subprocess

# Run the 'bjobs' command and capture its output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the standard output and error
output = result.stdout
error = result.stderr

# Check if there was any error
if result.returncode != 0:
    print(f"Error: {error}")
else:
    print(f"Output:\n{output}")
