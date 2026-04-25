
# Example: Install requests package
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

try:
    install('requests')
    print("Requests installed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
