
import subprocess

try:
    # Run the bjobs command
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Capture the output and error
    output = result.stdout
    error = result.stderr

    # Check if the command was successful
    if result.returncode == 0:
        print("Output:")
        print(output)
    else:
        print("Error:")
        print(error)

except Exception as e:
    print(f"An error occurred: {e}")
