
# Save this as install_packages.py
import subprocess
import sys

# List of packages to install
packages = ['requests', 'numpy']

for package in packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
