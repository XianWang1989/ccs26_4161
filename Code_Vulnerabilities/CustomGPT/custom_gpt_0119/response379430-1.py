
import subprocess

# Run the 'bjobs' command and capture the output
try:
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    # Decode the output from bytes to string
    output = stdout.decode('utf-8')
    error_output = stderr.decode('utf-8')

    if proc.returncode == 0:
        print("Command Output:")
        print(output)
    else:
        print("Error Output:")
        print(error_output)

except Exception as e:
    print(f"An error occurred: {e}")
