
import subprocess

# Use the shell=True option if needed
try:
    # Run the command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        print("Output of 'bjobs':")
        print(output)
    else:
        print("Error occurred:")
        print(result.stderr)

except Exception as e:
    print(f"An error occurred: {e}")
