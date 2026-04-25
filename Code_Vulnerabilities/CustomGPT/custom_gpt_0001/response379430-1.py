
import subprocess

try:
    # Run the bjobs command
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # Capture the standard output and standard error
    output = result.stdout
    error = result.stderr

    # Display the output
    if output:
        print("Output from bjobs:")
        print(output)
    if error:
        print("Error from bjobs:")
        print(error)

except subprocess.CalledProcessError as e:
    print(f"An error occurred while running bjobs: {e}")
    print(f"Return Code: {e.returncode}")
    print(f"Output: {e.output}")
    print(f"Error: {e.stderr}")
