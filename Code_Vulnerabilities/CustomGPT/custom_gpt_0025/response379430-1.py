
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Store the output
output = result.stdout
error = result.stderr

# Print the captured output and error (if any)
print("Output:")
print(output)
if error:
    print("Error:")
    print(error)
