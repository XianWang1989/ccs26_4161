
import subprocess

try:
    # Run the command
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    # Decode the output from bytes to string
    output = stdout.decode('utf-8')

    # Check for any errors
    if proc.returncode != 0:
        print("Error:", stderr.decode('utf-8'))
    else:
        print("Output:\n", output)

except Exception as e:
    print("An error occurred:", str(e))
