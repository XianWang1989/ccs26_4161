
import subprocess

try:
    # Run the bjobs command
    result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)

    # Get the stdout and stderr
    output = result.stdout
    error = result.stderr

    # Print output or handle it as needed
    if output:
        print("Output:")
        print(output)
    if error:
        print("Error:")
        print(error)

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
