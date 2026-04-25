
import subprocess

# Example command to install a package
package_name = "requests"

try:
    result = subprocess.run(["pip", "install", package_name], check=True)
    print(f"Successfully installed {package_name}.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
