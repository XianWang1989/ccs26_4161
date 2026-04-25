
import subprocess
import sys

def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing {package_name}: {e}")

# Example usage
install_package('numpy')  # Replace 'numpy' with the package you want to install
