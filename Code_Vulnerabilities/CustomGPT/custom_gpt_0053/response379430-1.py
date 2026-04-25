
import subprocess

try:
    # Run the bjobs command
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture the output and any error messages
    stdout, stderr = proc.communicate()

    # Decode the output from bytes to string (if needed)
    output = stdout.decode('utf-8')
    error = stderr.decode('utf-8')

    if proc.returncode == 0:
        print("Output:")
        print(output)
    else:
        print("Error:")
        print(error)

except Exception as e:
    print(f"An error occurred: {e}")
