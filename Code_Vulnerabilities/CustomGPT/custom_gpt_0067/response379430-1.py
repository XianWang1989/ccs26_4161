
import subprocess

try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.stderr}")
