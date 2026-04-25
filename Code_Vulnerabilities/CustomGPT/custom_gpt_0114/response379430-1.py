
import subprocess

# Run the 'bjobs' command and capture its output
try:
    result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)
    output = result.stdout  # Capture the standard output
    print(output)  # Print or use the output variable as needed
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
