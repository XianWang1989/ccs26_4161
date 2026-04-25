
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful and capture the output
if result.returncode == 0:
    output = result.stdout
else:
    output = result.stderr

# Print the captured output
print(output)
