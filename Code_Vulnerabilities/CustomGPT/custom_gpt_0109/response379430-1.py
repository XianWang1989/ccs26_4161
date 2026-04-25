
import subprocess

# Run the bjobs command
try:
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = proc.communicate()

    # Check if there was any error
    if proc.returncode != 0:
        print(f"Error: {stderr}")
    else:
        # Output captured into stdout
        print(stdout)

except Exception as e:
    print(f"An error occurred: {e}")
