
import subprocess

# Install a package using pip
try:
    subprocess.check_call(['python', '-m', 'pip', 'install', 'package_name'])
except Exception as e:
    print(f"An error occurred: {e}")
