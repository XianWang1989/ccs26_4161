
import subprocess

try:
    # Check pip version
    subprocess.run(["pip", "--version"], check=True)

    # List installed packages
    subprocess.run(["pip", "list"], check=True)

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
