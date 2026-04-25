
import subprocess

# Run the bjobs command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout.strip()  # Get the output from stdout
        print(output)  # Print the captured output
    else:
        print("Error:", result.stderr.strip())  # Print any error message

except Exception as e:
    print("An error occurred:", str(e))
