
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

try:
    install('numpy')  # Example package
    print("Package installed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
