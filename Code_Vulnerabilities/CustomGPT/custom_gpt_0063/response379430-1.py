
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful
if result.returncode == 0:
    output = result.stdout
    print(output)  # Output from the bjobs command
else:
    print("Error:", result.stderr)  # Print the error message if the command failed
