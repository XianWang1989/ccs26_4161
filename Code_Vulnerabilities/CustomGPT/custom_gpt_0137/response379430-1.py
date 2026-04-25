
import subprocess

try:
    # Run the command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # Obtain the output and errors (if any)
    output = result.stdout
    error = result.stderr

    # Print the captured output
    print("Output:\n", output)

    # Print any error messages (if any)
    if error:
        print("Error:\n", error)

except subprocess.CalledProcessError as e:
    print("An error occurred while trying to run the command:", e)
