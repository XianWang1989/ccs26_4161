
import subprocess

try:
    # Using subprocess.check_output to capture the output
    output = subprocess.check_output(['bjobs'], stderr=subprocess.STDOUT)
    # Decoding the bytes to string (if you're using Python 3)
    output_str = output.decode('utf-8')
    print(output_str)  # Now you have the output in the variable
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e.output.decode('utf-8')}")
