
import subprocess

def capture_bjobs_output():
    try:
        # Run the 'bjobs' command and capture the output
        result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if there was an error
        if result.returncode != 0:
            print("Error:", result.stderr)
            return None

        # Return the output
        return result.stdout.strip()  # Stripping any extra whitespace

    except Exception as e:
        print("An error occurred:", e)
        return None

output = capture_bjobs_output()
if output:
    print("bjobs output:\n", output)
