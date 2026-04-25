
import subprocess

# Run the LSF command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capture standard output and standard error
output = result.stdout
error = result.stderr

# Print the outputs
print("Output:", output)
print("Error:", error)
