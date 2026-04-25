
import subprocess

try:
    # Run the 'bjobs' command
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Capture the output and error
    stdout, stderr = proc.communicate()

    # Decode the output from bytes to string
    output = stdout.decode('utf-8')

    # Print the output or handle it as needed
    print(output)

    # Check if there's any error
    if stderr:
        error_message = stderr.decode('utf-8')
        print(f"Error: {error_message}")

except Exception as e:
    print(f"An error occurred: {e}")
