
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # Get the standard output and error
    output = result.stdout
    error = result.stderr

    # Print the captured output
    if output:
        print("Output:", output)
    if error:
        print("Error:", error)

except subprocess.CalledProcessError as e:
    print("An error occurred:", e)
