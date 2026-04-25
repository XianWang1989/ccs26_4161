
import subprocess

# Run the bjobs command and capture its output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Store the output in a variable
output = result.stdout

# Print the output
print(output)
