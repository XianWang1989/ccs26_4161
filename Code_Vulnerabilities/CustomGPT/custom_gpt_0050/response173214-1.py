
import subprocess

# Example to list installed packages
try:
    result = subprocess.check_output(['pip', 'list'], universal_newlines=True)
    print(result)
except subprocess.CalledProcessError as e:
    print("An error occurred:", e)
