
import subprocess

try:
    # Run the bjobs command and capture the output
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    # Decode the output bytes to string
    output = stdout.decode('utf-8')

    if proc.returncode == 0:
        print("Command Output:")
        print(output)  # Output stored in the variable
    else:
        print("Error Output:")
        print(stderr.decode('utf-8'))

except Exception as e:
    print(f"An error occurred: {e}")
