
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Access the output
output = result.stdout
error = result.stderr

# Print the output
print("Output:")
print(output)

# Print any error encountered
if error:
    print("Error:")
    print(error)
