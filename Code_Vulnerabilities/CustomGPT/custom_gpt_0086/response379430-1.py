
import subprocess

# Run the bjobs command and capture output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Store the output in a variable
output = result.stdout
error = result.stderr

# Print the output or error if exists
if output:
    print("Output:")
    print(output)
else:
    print("Error:")
    print(error)
