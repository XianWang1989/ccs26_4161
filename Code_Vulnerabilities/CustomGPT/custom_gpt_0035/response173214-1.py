
import sys
import subprocess

print("Python version:", sys.version)
print("Pip version:", subprocess.run(["pip", "--version"], capture_output=True, text=True).stdout)

# Install a package
subprocess.run(["pip", "install", "requests"])
