
import subprocess

try:
    # Using subprocess.run() (Python 3.5+)
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture stdout and stderr
    output = result.stdout
    error = result.stderr

    if result.returncode == 0:
        print("Output:")
        print(output)
    else:
        print("Error:")
        print(error)

except Exception as e:
    print(f"An error occurred: {e}")
