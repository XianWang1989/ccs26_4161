
import subprocess
import sys

# Example to install a package using pip
package_name = 'some_package_name'  # Replace with the actual package name

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
    print(f"{package_name} installed successfully!")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
