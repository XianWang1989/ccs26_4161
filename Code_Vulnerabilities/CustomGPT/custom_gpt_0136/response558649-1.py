
import subprocess
import sys

# Function to upgrade pip and install requests with security
def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyOpenSSL", "ndg-httpsclient", "pyasn1"])
        # For Python 3 users
        # subprocess.check_call([sys.executable, "-m", "pip", "install", "requests[security]"])
        print("All packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

install_packages()
