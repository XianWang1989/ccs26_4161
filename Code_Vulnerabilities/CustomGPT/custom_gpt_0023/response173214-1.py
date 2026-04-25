
import subprocess

# Example command to install a package using pip
package_name = "numpy"  # Replace with the package you want to install

try:
    subprocess.check_call(["pip", "install", package_name])
    print(f"{package_name} installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
