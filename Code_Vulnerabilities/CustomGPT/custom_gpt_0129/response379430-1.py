
import subprocess

# Use 'check_output' for capturing output directly into a variable
try:
    output = subprocess.check_output(['bjobs'], stderr=subprocess.STDOUT, universal_newlines=True)
    print(output)  # This will display the output of the bjobs command
except subprocess.CalledProcessError as e:
    print("An error occurred while running bjobs:")
    print(e.output)  # This prints the output from the command even if it failed
