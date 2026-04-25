
import subprocess

try:
    # Run the LSF command and capture output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        print("Command output:")
        print(output)
    else:
        print("Command failed:")
        print(result.stderr)

except Exception as e:
    print(f"An error occurred: {e}")
