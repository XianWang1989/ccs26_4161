
import subprocess

# Run the 'bjobs' command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the output from the result
output = result.stdout
error = result.stderr

# Check if there was an error
if error:
    print("Error:", error)
else:
    print("Output:", output)
