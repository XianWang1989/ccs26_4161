
import subprocess

def run_bjobs():
    try:
        # Run the bjobs command
        proc = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        # Decode the output from bytes to string
        output = stdout.decode('utf-8').strip()
        error = stderr.decode('utf-8').strip()

        if error:
            print("Error:", error)
        else:
            return output

    except Exception as e:
        print("An error occurred:", str(e))

# Capture output
job_status = run_bjobs()
if job_status:
    print("Job Status:\n", job_status)
