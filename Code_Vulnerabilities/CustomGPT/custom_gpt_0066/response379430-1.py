
import subprocess

try:
    # Run the 'bjobs' command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check for errors
    if result.returncode == 0:
        # Output is captured in result.stdout
        output = result.stdout
        print("Command Output:")
        print(output)
    else:
        # Handle errors if the command fails
        print("Error:")
        print(result.stderr)

except FileNotFoundError:
    print("The command 'bjobs' was not found. Please ensure it is installed and accessible.")
