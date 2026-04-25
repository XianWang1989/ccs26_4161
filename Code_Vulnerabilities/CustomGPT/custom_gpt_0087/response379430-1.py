
import subprocess

def get_bjobs_output():
    # Run the 'bjobs' command and capture the output
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    # Decode the output from bytes to string
    output = stdout.decode('utf-8')

    # Check for errors
    if proc.returncode != 0:
        error_message = stderr.decode('utf-8')
        print("Error:", error_message)
        return None

    return output

# Get the output and print it
bjobs_output = get_bjobs_output()
if bjobs_output:
    print(bjobs_output)
