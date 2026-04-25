
import subprocess

# Run the 'bjobs' command and capture outputs
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful
if result.returncode == 0:
    output = result.stdout  # Capture standard output
    print("Command output:")
    print(output)
else:
    print("Error:")
    print(result.stderr)  # Capture standard error output
