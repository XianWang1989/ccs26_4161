
import subprocess

# Use subprocess.run, which is more straightforward
try:
    result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)
    output = result.stdout
    print(output)  # Print the output to the variable
except subprocess.CalledProcessError as e:
    print(f"Error: {e.stderr}")  # Print any error messages
