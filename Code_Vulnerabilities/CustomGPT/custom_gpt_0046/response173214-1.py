
import subprocess

def install(package):
    subprocess.check_call(["python", "-m", "pip", "install", package])

# Example usage - replace 'requests' with the desired package
install('requests')
