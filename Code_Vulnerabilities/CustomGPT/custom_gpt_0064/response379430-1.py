
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check for errors
if result.stderr:
    print("Error:", result.stderr)
else:
    # Print the output
    output = result.stdout
    print("Output:\n", output)
