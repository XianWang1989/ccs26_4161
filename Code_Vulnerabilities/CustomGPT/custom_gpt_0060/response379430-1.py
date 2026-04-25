
import subprocess

# Use subprocess.run for more convenience and clarity
try:
    # Execute the command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout  # This will contain the output of 'bjobs'
        print("Output:")
        print(output)
    else:
        print("Error:")
        print(result.stderr)  # This will contain any error messages

except Exception as e:
    print(f"An error occurred: {e}")
