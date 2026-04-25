
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)

    # Access the standard output
    output = result.stdout
    print(output)  # Print the output

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.stderr}")
