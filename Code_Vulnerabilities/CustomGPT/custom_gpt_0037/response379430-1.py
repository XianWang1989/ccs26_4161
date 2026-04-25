
import subprocess

try:
    # Run the bjobs command
    result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)

    # Get the standard output
    output = result.stdout

    print("Command output:")
    print(output)

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.stderr}")
