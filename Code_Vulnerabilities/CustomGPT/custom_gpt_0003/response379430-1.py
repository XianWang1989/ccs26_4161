
import subprocess

# Using subprocess.run to get the output directly
try:
    # Execute the command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # The output will be in result.stdout
    output = result.stdout.strip()  # Remove any leading and trailing whitespace
    print("Output from bjobs:")
    print(output)

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.stderr.strip()}")  # Print any error message returned by the command
