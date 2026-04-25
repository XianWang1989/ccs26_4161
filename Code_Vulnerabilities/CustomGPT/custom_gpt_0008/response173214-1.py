
import os
import subprocess

# Check if pip is installed
try:
    subprocess.check_call(['pip', '--version'])
    print("pip is installed.")
except subprocess.CalledProcessError:
    print("pip is not installed. Please install pip.")

# Installing a package using pip
package_name = "requests"
try:
    subprocess.check_call(['pip', 'install', package_name])
    print(f"{package_name} installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while installing {package_name}: {e}")
