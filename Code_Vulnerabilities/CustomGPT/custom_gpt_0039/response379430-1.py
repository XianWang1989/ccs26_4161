
import subprocess

try:
    # Run the command and capture output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout  # Capture the output
        print("Output:\n", output)
    else:
        print("Error:\n", result.stderr)  # Capture and print any errors

except Exception as e:
    print("An error occurred:", e)
