
import subprocess

def run_bjobs():
    try:
        # Run the bjobs command
        result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Capture the output
            output = result.stdout
            return output
        else:
            # Capture any error messages
            error = result.stderr
            return f"Error: {error}"

    except Exception as e:
        return f"An exception occurred: {e}"

# Call the function and print the output
output = run_bjobs()
print(output)
