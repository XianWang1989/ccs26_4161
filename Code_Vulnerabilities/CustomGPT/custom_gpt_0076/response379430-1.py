
import subprocess

try:
    # Use subprocess.run to execute the command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout.strip()  # Get the output, removing any extra whitespace
        print("Output of bjobs:")
        print(output)
    else:
        print("Error running bjobs:", result.stderr.strip())

except Exception as e:
    print("An error occurred:", str(e))
