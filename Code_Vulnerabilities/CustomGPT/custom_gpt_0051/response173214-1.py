
import os
import subprocess

# Check Python Version
python_version = subprocess.run(['python', '--version'], capture_output=True, text=True)
print(f"Python Version: {python_version.stdout.strip()}")

# Check pip Version
pip_version = subprocess.run(['pip', '--version'], capture_output=True, text=True)
print(f"Pip Version: {pip_version.stdout.strip()}")

# Try to install a package to confirm pip is working
try:
    subprocess.run(['pip', 'install', 'requests'], check=True)
    print("Package 'requests' installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
