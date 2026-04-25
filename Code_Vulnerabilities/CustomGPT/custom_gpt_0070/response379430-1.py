
import subprocess

# Run the 'bjobs' command and capture the output
result = subprocess.run(['bjobs'], capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    output = result.stdout
    print("Output of bjobs:")
    print(output)
else:
    print("Error occurred:")
    print(result.stderr)
