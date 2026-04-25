
import subprocess

# Check pip version
pip_version = subprocess.run(["pip", "--version"], capture_output=True, text=True)
print("Pip version:", pip_version.stdout)

# Trying to install a package
try:
    subprocess.run(["pip", "install", "requests"], check=True)
    print("Package installed successfully.")
except subprocess.CalledProcessError as e:
    print("Error during installation:", e)
