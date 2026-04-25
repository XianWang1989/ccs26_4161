
import subprocess

# Run the bjobs command
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capture stdout and stderr
output = result.stdout
error = result.stderr

# Print the output and error (if any)
print("Output:")
print(output)

if error:
    print("Error:")
    print(error)
