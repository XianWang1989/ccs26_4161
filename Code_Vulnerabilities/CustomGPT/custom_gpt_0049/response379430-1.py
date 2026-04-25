
import subprocess

def get_bjobs_output():
    try:
        # Run the bjobs command
        proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Capture stdout and stderr
        stdout, stderr = proc.communicate()

        # Check if any error occurred
        if proc.returncode != 0:
            raise Exception(f"Error running bjobs: {stderr.decode().strip()}")

        # Decode the output
        output = stdout.decode().strip()

        return output

    except Exception as e:
        return str(e)

# Example usage
output = get_bjobs_output()
print(output)
