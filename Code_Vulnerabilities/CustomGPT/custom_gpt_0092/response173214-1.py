
import subprocess

def install_package(package):
    subprocess.check_call(["python", '-m', 'pip', 'install', package])

# Example usage
install_package('requests')
