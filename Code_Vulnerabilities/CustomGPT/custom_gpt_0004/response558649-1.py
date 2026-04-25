
import sys
import subprocess

# Check Python version
if sys.version_info[0] < 3:
    print("Please upgrade to Python 3.x.")
else:
    # Upgrade pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

    # Install requests[security]
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests[security]"])

print("Installation complete!")
