
import subprocess

def get_bjobs_output():
    try:
        # Run the bjobs command and capture the output
        result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            return result.stdout  # Capture the standard output
        else:
            print(f"Error: {result.stderr}")  # Capture any errors
            return None

    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

# Usage
output = get_bjobs_output()
if output:
    print(output)
