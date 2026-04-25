
import subprocess

# Using subprocess.run (recommended for simplicity)
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
    else:
        output = f"Error: {result.stderr}"

    print(output)

except Exception as e:
    print(f"An error occurred: {e}")
