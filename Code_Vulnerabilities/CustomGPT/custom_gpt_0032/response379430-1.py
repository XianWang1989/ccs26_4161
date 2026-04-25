
import subprocess

try:
    # Execute the bjobs command
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture the output and error messages
    stdout, stderr = proc.communicate()

    # Decode the output from bytes to string
    output = stdout.decode('utf-8')
    error = stderr.decode('utf-8')

    # Print the output or handle errors
    if output:
        print("Output:")
        print(output)
    if error:
        print("Error:")
        print(error)

except Exception as e:
    print(f"An error occurred: {e}")
