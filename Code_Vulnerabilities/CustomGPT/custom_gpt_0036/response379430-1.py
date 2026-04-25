
import subprocess

try:
    # Execute the command and capture the output
    output = subprocess.check_output(['bjobs'], stderr=subprocess.STDOUT)

    # Decode the byte string to a regular string
    output = output.decode('utf-8')

    # Print the captured output
    print(output)
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.output.decode('utf-8')}")
