
import subprocess

try:
    # Execute the command and capture the output
    output = subprocess.check_output(['bjobs'], stderr=subprocess.STDOUT, text=True)

    # Print the captured output
    print(output)
except subprocess.CalledProcessError as e:
    # Handle errors in the command execution
    print(f"Error executing command: {e.output}")
