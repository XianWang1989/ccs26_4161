
import subprocess

try:
    # Run the bjobs command and capture the output
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    # Decode the output from bytes to string, if needed
    output = stdout.decode('utf-8')
    error = stderr.decode('utf-8')

    if proc.returncode == 0:
        # Successfully captured output
        print("Output of bjobs command:")
        print(output)
    else:
        # There was an error while running the command
        print("Error:", error)

except Exception as e:
    print("An error occurred:", str(e))
