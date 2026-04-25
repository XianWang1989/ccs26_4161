
import subprocess

try:
    # Run the command and capture output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout  # This will contain the command output
        print(output)
    else:
        print(f"Error: {result.stderr}")  # This will contain the error message

except Exception as e:
    print(f"An error occurred: {e}")
