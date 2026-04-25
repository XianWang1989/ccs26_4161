
import subprocess

def get_bjobs_output():
    result = subprocess.run(['bjobs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        output = result.stdout
        print(output)
    else:
        print(f"Error: {result.stderr}")

get_bjobs_output()
