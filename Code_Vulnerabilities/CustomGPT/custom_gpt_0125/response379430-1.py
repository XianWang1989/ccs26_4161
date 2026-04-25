
import subprocess

try:
    # Using subprocess.run which is recommended for most cases
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful and capture the output
    if result.returncode == 0:
        output = result.stdout
        print("Output captured successfully:")
        print(output)
    else:
        print("Error occurred while running bjobs:")
        print(result.stderr)
except Exception as e:
    print(f"An error occurred: {e}")
