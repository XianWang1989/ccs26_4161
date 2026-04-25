
import subprocess

# Using subprocess.run to capture output
try:
    result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)
    output = result.stdout  # Capturing standard output
    print(output)  # Print the output
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.stderr}")  # Print any error messages
