
import subprocess

# Execute the 'bjobs' command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Store the command output in a variable
        output = result.stdout
        print("Output of 'bjobs':")
        print(output)
    else:
        print(f"Error executing command: {result.stderr}")

except FileNotFoundError:
    print("The command 'bjobs' was not found. Please ensure it is available in the environment.")
except Exception as e:
    print(f"An error occurred: {e}")
