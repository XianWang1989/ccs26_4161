
import subprocess

# Run the bjobs command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout.strip()  # Capture stdout and remove any trailing whitespace
    print(output)  # Print the output directly
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.stderr.strip()}")  # Capture any errors
