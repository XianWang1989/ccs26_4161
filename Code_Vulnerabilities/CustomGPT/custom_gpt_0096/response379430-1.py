
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check for errors
if result.returncode == 0:
    output = result.stdout
else:
    output = result.stderr

print(output)
