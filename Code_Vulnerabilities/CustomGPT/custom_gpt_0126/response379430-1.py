
import subprocess

try:
    # Running the bjobs command and capturing the output
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        print("Output of bjobs command:")
        print(output)
    else:
        print("Error occurred:")
        print(result.stderr)

except Exception as e:
    print(f"An error occurred: {e}")
