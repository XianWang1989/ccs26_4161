
import subprocess

# Run the bjobs command and capture output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    # Access stdout and stderr
    output = result.stdout
    error = result.stderr

    if output:
        print("Output of bjobs:")
        print(output)
    if error:
        print("Error output:")
        print(error)

except subprocess.CalledProcessError as e:
    print(f"An error occurred while running bjobs: {e}")
