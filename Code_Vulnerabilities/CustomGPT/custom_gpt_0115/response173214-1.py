
import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Example usage
try:
    install('numpy')  # Replace 'numpy' with your desired package
    print("Installation successful.")
except Exception as e:
    print(f"An error occurred: {e}")
