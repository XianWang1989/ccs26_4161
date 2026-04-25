
import subprocess

try:
    # Run the command and capture the output
    result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)

    # Get the standard output
    output = result.stdout

    # Print the output
    print(output)
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
