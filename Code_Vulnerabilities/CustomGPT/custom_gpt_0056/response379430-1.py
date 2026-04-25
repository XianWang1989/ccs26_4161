
import subprocess

# Run the bjobs command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Access the output and error messages
output = result.stdout
error = result.stderr

# Print the output
if output:
    print("Output:\n", output)
else:
    print("No output.")

# Print any errors
if error:
    print("Error:\n", error)
