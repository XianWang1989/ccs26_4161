
import subprocess

# Using subprocess.run()
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Output the command's stdout and stderr
output = result.stdout
error = result.stderr

print("Output:\n", output)
print("Error:\n", error)
