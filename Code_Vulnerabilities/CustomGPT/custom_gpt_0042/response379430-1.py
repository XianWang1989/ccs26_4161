
import subprocess

# Run the bjobs command and capture its output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout  # Capture the standard output
        print(output)
    else:
        print(f"Error executing bjobs: {result.stderr}")

except Exception as e:
    print(f"An error occurred: {e}")
