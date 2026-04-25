
import subprocess

# Running the bjobs command
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout.strip()  # Capture the output
    error = result.stderr.strip()    # Capture any errors

    if result.returncode == 0:
        print("Output:\n", output)
    else:
        print("Error:\n", error)
except Exception as e:
    print("An error occurred:", str(e))
