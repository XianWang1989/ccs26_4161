
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if there was an error
if result.returncode == 0:
    output = result.stdout  # This will contain the output of the command
    print(output)
else:
    print(f"Error occurred: {result.stderr}")
