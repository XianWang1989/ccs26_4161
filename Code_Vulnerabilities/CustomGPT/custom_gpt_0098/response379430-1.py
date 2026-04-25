
import subprocess

# Run the LSF command 'bjobs' and capture the output
try:
    proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    # Decode the output from bytes to string
    output = stdout.decode('utf-8').strip()

    # Check if there were any errors
    if stderr:
        print("Error:", stderr.decode('utf-8').strip())
    else:
        print("Output:", output)

except Exception as e:
    print("An error occurred:", str(e))
