
import subprocess

# Run the bjobs command and capture output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Get the output
output = result.stdout
error = result.stderr

# Print the output
print("Output:")
print(output)

# Print any errors
if error:
    print("Errors:")
    print(error)
