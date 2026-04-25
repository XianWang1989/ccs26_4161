
import subprocess

# Run the 'bjobs' command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        print("Output captured:")
        print(output)
    else:
        print("Error during execution:")
        print(result.stderr)

except Exception as e:
    print(f"An error occurred: {e}")
