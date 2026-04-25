
import subprocess

# Run the bjobs command
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if there was an error
if result.returncode == 0:
    output = result.stdout  # Capture the output
else:
    output = result.stderr  # Capture the error output

# Print the output
print(output)
