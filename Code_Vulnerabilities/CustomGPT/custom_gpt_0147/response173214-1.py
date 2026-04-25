
import subprocess

def check_pip_installation(package_name):
    try:
        subprocess.run(['pip', 'install', package_name], check=True)
        print(f"{package_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during installation: {e}")

if __name__ == "__main__":
    # Example package to install
    check_pip_installation('numpy')  # Replace with any package you require
