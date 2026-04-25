
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # Get the output and error (if any)
    output = result.stdout
    error = result.stderr

    # Print the output
    print("Output:")
    print(output)

    # Print errors if there's any
    if error:
        print("Error:")
        print(error)

except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")
