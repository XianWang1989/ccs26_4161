
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Output of the command
        output = result.stdout
        print(output)
    else:
        # If there's an error, print the stderr
        print("Error:", result.stderr)
except Exception as e:
    print("An error occurred:", e)
