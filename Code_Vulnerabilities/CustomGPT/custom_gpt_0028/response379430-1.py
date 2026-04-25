
import subprocess

def get_bjobs_output():
    try:
        # Run the 'bjobs' command and capture the output
        result = subprocess.run(['bjobs'], capture_output=True, text=True, check=True)

        # Access the standard output
        output = result.stdout
        return output

    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        print(f"An error occurred: {e}")
        return None

# Example usage
bjobs_output = get_bjobs_output()
if bjobs_output:
    print("bjobs output:")
    print(bjobs_output)
