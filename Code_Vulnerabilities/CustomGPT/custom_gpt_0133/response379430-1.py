
import subprocess

try:
    # Using subprocess.run for a simpler approach
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Capturing standard output
        output = result.stdout
        print("Captured Output:\n", output)
    else:
        print("Error occurred:\n", result.stderr)
except FileNotFoundError:
    print("The command 'bjobs' was not found. Please ensure it is installed and in your PATH.")
except Exception as e:
    print(f"An error occurred: {e}")
