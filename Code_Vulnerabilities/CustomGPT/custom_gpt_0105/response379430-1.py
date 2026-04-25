
import subprocess

def get_bjobs_output():
    try:
        # Run the bjobs command
        result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if there was an error
        if result.returncode != 0:
            print("Error:", result.stderr)
            return None

        # Capture the command output
        output = result.stdout
        return output

    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage
output = get_bjobs_output()
if output is not None:
    print("bjobs output:\n", output)
