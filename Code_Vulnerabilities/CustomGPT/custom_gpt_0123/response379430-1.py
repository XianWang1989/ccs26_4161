
import subprocess

try:
    # Using subprocess.run() to capture output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        print("Output:")
        print(output)
    else:
        print("Error:", result.stderr)

except FileNotFoundError:
    print("The command 'bjobs' was not found. Make sure it is installed.")
except Exception as e:
    print("An error occurred:", e)
