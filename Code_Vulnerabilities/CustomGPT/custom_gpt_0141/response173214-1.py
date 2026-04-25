
import subprocess

# Function to install a package using pip
def install_package(package):
    try:
        subprocess.check_call(["pip", "install", package])
        print(f"{package} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing {package}: {e}")

# Example usage
if __name__ == "__main__":
    install_package('requests')  # Replace 'requests' with any package you want to install
