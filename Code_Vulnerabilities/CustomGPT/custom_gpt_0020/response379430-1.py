
import subprocess

# Run the 'bjobs' command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Output successfully captured
    output = result.stdout
    print("Output of bjobs command:")
    print(output)
else:
    # Handle errors
    print("Error running bjobs command:")
    print(result.stderr)
