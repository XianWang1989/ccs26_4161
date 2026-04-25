
import subprocess

try:
    # Run the 'bjobs' command
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Capture the standard output
        output = result.stdout
        print("Output of bjobs:\n", output)
    else:
        print("Error:", result.stderr)

except Exception as e:
    print("An error occurred:", str(e))
