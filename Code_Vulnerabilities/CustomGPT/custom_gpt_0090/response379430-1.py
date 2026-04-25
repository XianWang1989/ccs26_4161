
import subprocess

# Run the bjobs command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout  # Get the standard output
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.stderr}")
