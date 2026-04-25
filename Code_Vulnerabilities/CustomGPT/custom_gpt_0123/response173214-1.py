
import subprocess
import sys

# Check if pip is installed
try:
    import pip
    print("pip is installed.")
except ImportError:
    print("pip is not installed. Installing pip...")
    subprocess.check_call([sys.executable, '-m', 'ensurepip'])

# Install a package using pip
package_name = 'requests'
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
    print(f"{package_name} installed successfully.")
except subprocess.CalledProcessError:
    print(f"Failed to install {package_name}.")
