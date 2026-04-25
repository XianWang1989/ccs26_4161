
import subprocess

try:
    # Use subprocess.run for a simpler interface
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # Get the standard output
    output = result.stdout

    # Print the captured output
    print(output)

except subprocess.CalledProcessError as e:
    print("Error executing command:", e.stderr)
