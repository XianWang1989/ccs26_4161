
import subprocess

# Run the 'bjobs' command and capture its output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        print("Command Output:\n", output)
    else:
        print("Error:\n", result.stderr)

except Exception as e:
    print("An error occurred:", e)
