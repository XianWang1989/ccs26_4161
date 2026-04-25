
import subprocess

try:
    # Run the bjobs command
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture the output and errors
    output = result.stdout
    errors = result.stderr

    # Check if there were any errors
    if result.returncode == 0:
        print("Output:")
        print(output)
    else:
        print("Errors:")
        print(errors)

except Exception as e:
    print(f"An error occurred: {e}")
