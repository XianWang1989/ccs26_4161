
import subprocess

# Replace 'some_package' with the actual package name you want to install
package_name = "requests"

try:
    subprocess.check_call(["pip", "install", package_name])
    print(f"{package_name} installed successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while installing {package_name}: {e}")
