
import subprocess

# Run the bjobs command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout  # Get the output
    error = result.stderr    # Get any errors if occurred

    print("Output:\n", output)
    if error:
        print("Error:\n", error)

except subprocess.CalledProcessError as e:
    print("An error occurred while running bjobs:", e)
