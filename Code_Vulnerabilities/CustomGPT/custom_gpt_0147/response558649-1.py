
import os
import subprocess
import sys

# Assuming you are using a shell like bash or zsh
def install_requests_security():
    # Set the necessary environment variable if on Linux
    os.environ['PROCESSOR_ARCHITECTURE'] = 'x86'  # or 'AMD64' depending on your architecture

    # Upgrade pip
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

    # Install requests with security extras
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests[security]'])

if __name__ == "__main__":
    install_requests_security()
