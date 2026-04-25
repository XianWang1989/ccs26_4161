
import subprocess

try:
    # Run the bjobs command
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture the output
    output = result.stdout
    error = result.stderr

    if result.returncode == 0:
        # If the command was successful, print the output
        print('Output:', output)
    else:
        # If there was an error, print the error
        print('Error:', error)

except Exception as e:
    print('An error occurred:', str(e))
