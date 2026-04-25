
import subprocess

try:
    # Run the bjobs command and capture the output
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    # Decode the output to convert bytes to string
    output = stdout.decode('utf-8')
    error_output = stderr.decode('utf-8')

    # Check for errors
    if proc.returncode != 0:
        print("Error:", error_output)
    else:
        print("bjobs output:")
        print(output)

except Exception as e:
    print("An error occurred:", e)
