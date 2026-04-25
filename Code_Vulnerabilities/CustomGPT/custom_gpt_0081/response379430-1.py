
import subprocess

# Run the LSF command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if there was an error
    if result.returncode != 0:
        print("Error:", result.stderr)
    else:
        # Output captured in result.stdout
        output = result.stdout
        print("Command Output:\n", output)

except Exception as e:
    print("An error occurred:", str(e))
