
import subprocess

# Run the bjobs command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout
    print(output)  # This will display the output of the bjobs command
except subprocess.CalledProcessError as e:
    print("Error:", e.stderr)
