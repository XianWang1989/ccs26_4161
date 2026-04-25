
import subprocess

try:
    # Run the 'bjobs' command
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture the standard output and error
    output = result.stdout
    error = result.stderr

    # Check if there's any error and print accordingly
    if result.returncode != 0:
        print(f"Error: {error}")
    else:
        print(f"Output:\n{output}")

except Exception as e:
    print(f"An error occurred: {e}")
