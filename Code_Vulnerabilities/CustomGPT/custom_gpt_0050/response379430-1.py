
import subprocess

try:
    # Run the bjobs command and capture the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        print("Output from bjobs:")
        print(output)
    else:
        print("Error:", result.stderr)

except Exception as e:
    print(f"An error occurred: {e}")
