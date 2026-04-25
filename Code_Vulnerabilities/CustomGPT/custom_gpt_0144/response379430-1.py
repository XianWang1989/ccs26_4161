import subprocess

# Run the command and capture output
process = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Decode the output (Python 3)
output = stdout.decode('utf-8')

print("Captured Output:")
print(output)
