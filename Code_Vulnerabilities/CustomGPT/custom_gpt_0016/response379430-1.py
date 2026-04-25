
import subprocess

try:
    # Run the bjobs command
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        print("Output of bjobs:\n", output)
    else:
        print("Error occurred:\n", result.stderr)

except Exception as e:
    print(f"An exception occurred: {e}")
