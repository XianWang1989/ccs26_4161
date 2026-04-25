
import subprocess

# Run the bjobs command
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capture the output and error
output = result.stdout
error = result.stderr

# Check if there is an error
if result.returncode != 0:
    print(f"Error running bjobs: {error}")
else:
    # Successfully captured the output
    print("Output of bjobs command:")
    print(output)
