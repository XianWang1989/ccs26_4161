
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check for errors
if result.returncode != 0:
    print(f"Error: {result.stderr}")
else:
    # Get the output
    output = result.stdout
    print(output)
