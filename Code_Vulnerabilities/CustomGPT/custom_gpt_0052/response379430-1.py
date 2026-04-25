
import subprocess

# Run the 'bjobs' command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful
if result.returncode == 0:
    output = result.stdout
    print("Command Output:")
    print(output)
else:
    print("Error occurred:")
    print(result.stderr)
