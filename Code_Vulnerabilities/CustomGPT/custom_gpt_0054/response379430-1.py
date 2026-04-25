
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Store the output in a variable
    output = result.stdout
    print("Output from bjobs:")
    print(output)
else:
    print("Error running bjobs:")
    print(result.stderr)
