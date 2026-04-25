
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check for errors
    if result.returncode == 0:
        # Capture the standard output
        output = result.stdout
        print(output)
    else:
        print(f"Error: {result.stderr}")
except Exception as e:
    print(f"An exception occurred: {e}")
