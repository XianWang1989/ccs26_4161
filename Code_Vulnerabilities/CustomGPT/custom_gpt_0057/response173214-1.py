
import subprocess
import sys

def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("Updated pip successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    install_packages()
