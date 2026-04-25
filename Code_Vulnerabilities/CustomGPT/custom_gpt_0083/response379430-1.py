
import subprocess

# Run the bjobs command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout  # Capture the standard output
    print(output)  # Print the output
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.stderr}")
