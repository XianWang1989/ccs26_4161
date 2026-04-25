
import subprocess

try:
    # Running the LSF command and capturing the output
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    # Decoding the output to a string (if needed) and handling errors
    if proc.returncode == 0:
        output = stdout.decode('utf-8')  # Decode bytes to string
        print("Output of bjobs command:")
        print(output)
    else:
        print("Error occurred:")
        error_message = stderr.decode('utf-8')
        print(error_message)

except Exception as e:
    print(f"An exception occurred: {e}")
