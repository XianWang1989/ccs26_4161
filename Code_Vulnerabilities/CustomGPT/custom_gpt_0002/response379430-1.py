
import subprocess

try:
    output = subprocess.check_output(['bjobs'], stderr=subprocess.STDOUT)
    output = output.decode('utf-8')  # Decode the byte output
    print(output)  # Now you have the output in a variable
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.output.decode('utf-8')}")
