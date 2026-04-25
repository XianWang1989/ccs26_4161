
import subprocess

def get_bjobs_output():
    # Run the command and capture the output
    try:
        result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout
        return output.strip()  # Remove any trailing newlines or spaces
    except subprocess.CalledProcessError as e:
        # Handle errors in command execution
        print("Error executing bjobs:", e.stderr)
        return None

if __name__ == "__main__":
    bjobs_output = get_bjobs_output()
    if bjobs_output:
        print("bjobs output:")
        print(bjobs_output)
    else:
        print("No output or command failed.")
