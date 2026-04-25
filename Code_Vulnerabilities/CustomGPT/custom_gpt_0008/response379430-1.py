
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the standard output
output = result.stdout

# Check for errors
if result.returncode != 0:
    error = result.stderr
    print(f"Error: {error}")
else:
    print(f"Output:\n{output}")
