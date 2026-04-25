
import subprocess

# Run the 'bjobs' command and capture the output
try:
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    output = result.stdout  # This is where the output is stored
    error = result.stderr    # This captures any error messages

    # Check if there are errors
    if error:
        print("Error occurred:", error)

    # Print the output
    print("Output of bjobs:")
    print(output)

except subprocess.CalledProcessError as e:
    print(f'An error occurred while executing bjobs: {e}')
