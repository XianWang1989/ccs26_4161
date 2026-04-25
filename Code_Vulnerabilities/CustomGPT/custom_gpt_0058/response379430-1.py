
import subprocess

try:
    # Run the bjobs command and capture the output
    output = subprocess.check_output(['bjobs'], stderr=subprocess.PIPE)

    # Decode the byte string to a regular string
    output_str = output.decode('utf-8')

    # Print the output
    print(output_str)

except subprocess.CalledProcessError as e:
    # Handle errors in command execution
    print(f"An error occurred: {e}")
    print(f"Command output: {e.output.decode('utf-8')}")
