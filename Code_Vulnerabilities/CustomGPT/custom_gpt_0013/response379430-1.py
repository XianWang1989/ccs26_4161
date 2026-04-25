
import subprocess

try:
    # Run the 'bjobs' command
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture the output and errors
    stdout, stderr = proc.communicate()

    # Check if the command was successful
    if proc.returncode == 0:
        print("Command output:")
        print(stdout)
    else:
        print("Error:")
        print(stderr)

except Exception as e:
    print(f"An error occurred: {e}")
