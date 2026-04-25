
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Output captured in result.stdout
        output = result.stdout
        print(output)
    else:
        # If there was an error, output the error message
        print(f"Error: {result.stderr}")

except Exception as e:
    print(f"An error occurred: {e}")
