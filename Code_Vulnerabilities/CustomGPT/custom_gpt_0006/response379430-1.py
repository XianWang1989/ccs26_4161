
import subprocess

# Using subprocess.run() with text=True to capture output as a string
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout
    error = result.stderr

    if output:
        print("Output from bjobs:")
        print(output)
    if error:
        print("Error from bjobs:")
        print(error)

except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode} and error: {e.stderr}")
