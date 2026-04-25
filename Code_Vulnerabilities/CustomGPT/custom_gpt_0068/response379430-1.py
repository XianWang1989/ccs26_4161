
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout  # Capture the output
        print("Output of bjobs command:")
        print(output)
    else:
        print("Error executing bjobs:")
        print(result.stderr)  # Capture and print any error output

except Exception as e:
    print(f"An error occurred: {e}")
