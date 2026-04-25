
import subprocess

# Using subprocess.run
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout
    print("bjobs output:")
    print(output)
except subprocess.CalledProcessError as e:
    print("Error:", e.stderr)
