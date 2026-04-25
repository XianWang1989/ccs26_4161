
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout  # Capture the standard output
        print(output)  # Print the output
    else:
        error = result.stderr  # Capture any errors
        print(f"Error: {error}")

except Exception as e:
    print(f"An error occurred: {e}")
