
import subprocess
import sys

# Function to check pip version
def check_pip():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'])
        print("pip is installed correctly.")
    except subprocess.CalledProcessError:
        print("pip installation is missing.")

# Function to install a package
def install_package(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Check pip and install a package
check_pip()
install_package('requests')  # Replace 'requests' with your desired package
