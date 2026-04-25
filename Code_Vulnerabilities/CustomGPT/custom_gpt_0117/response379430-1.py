
import subprocess

try:
    # Run the 'bjobs' command
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout  # Get the standard output
        print("Output:\n", output)
    else:
        print("Error:\n", result.stderr)  # Get the error output if there's an issue

except FileNotFoundError:
    print("The command 'bjobs' was not found. Please ensure it is installed.")
