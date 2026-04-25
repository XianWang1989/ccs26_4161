
import subprocess

# Run the bjobs command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # Output is in result.stdout
    output = result.stdout
    error = result.stderr

    # Print the results
    if output:
        print("Output:\n", output)
    if error:
        print("Error:\n", error)
except subprocess.CalledProcessError as e:
    print("Command failed with return code:", e.returncode)
    print("Error output:", e.stderr)
