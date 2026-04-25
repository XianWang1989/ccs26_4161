
import subprocess

# Run the command and capture the output
result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check for errors
if result.returncode != 0:
    print("Error:", result.stderr)
else:
    # Output captured in result.stdout
    output = result.stdout
    print(output)
