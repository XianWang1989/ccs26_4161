
import subprocess

try:
    # Execute the command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # Get the output and error (if any)
    output = result.stdout
    error = result.stderr

    if output:
        print("Output:\n", output)
    if error:
        print("Error:\n", error)

except subprocess.CalledProcessError as e:
    print("Command failed with exit code:", e.returncode)
    print("Error output:\n", e.stderr)
