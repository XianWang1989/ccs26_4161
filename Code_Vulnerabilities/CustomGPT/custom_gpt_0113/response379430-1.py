
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check for errors
if result.returncode == 0:
    # Capture the output into a variable
    output = result.stdout
    print("Output:")
    print(output)
else:
    # Print error message
    print("Error:", result.stderr)
