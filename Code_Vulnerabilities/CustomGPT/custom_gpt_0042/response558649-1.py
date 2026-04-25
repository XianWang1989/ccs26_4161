
import subprocess
import sys

def upgrade_package(package_name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', package_name])

# Upgrade pip and setuptools
upgrade_package('pip')
upgrade_package('setuptools')

# Install requests with security features
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests[security]'])
