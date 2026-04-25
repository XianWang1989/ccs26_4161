
# Upgrade pip and setuptools, then install requests with security extras
import os
import sys
import subprocess

def install_requests_with_security():
    try:
        # Upgrade pip and setuptools to the latest version
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip', 'setuptools'])

        # Install requests with security
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests[security]'])

        print("Installation successful!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_requests_with_security()
