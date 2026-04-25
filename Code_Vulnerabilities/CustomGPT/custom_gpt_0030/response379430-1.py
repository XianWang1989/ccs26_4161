
import subprocess

def get_bjobs_output():
    try:
        # Run the bjobs command and capture the output
        result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            return result.stdout.strip()  # Return the output without extra whitespace
        else:
            raise RuntimeError(f"Error: {result.stderr.strip()}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
output = get_bjobs_output()
print(output)
