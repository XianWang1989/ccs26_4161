
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful
if result.returncode == 0:
    output = result.stdout
    print("Output of bjobs:\n", output)
else:
    print("Error running bjobs:\n", result.stderr)
