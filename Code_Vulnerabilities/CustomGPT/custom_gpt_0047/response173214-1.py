
import subprocess
import sys

# Check pip version
subprocess.check_call([sys.executable, '-m', 'pip', '--version'])

# Install a package, e.g., numpy
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])
