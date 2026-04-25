
import subprocess

try:
    # Run the 'bjobs' command and capture output
    result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)

    # Get the output from stdout
    output = result.stdout
    print(output)  # Output of the 'bjobs' command

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.stderr}")
