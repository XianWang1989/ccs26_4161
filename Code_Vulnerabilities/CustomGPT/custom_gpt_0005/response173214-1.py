
import subprocess

def check_pip():
    try:
        # Check pip version
        pip_version = subprocess.check_output(['pip', '--version'])
        print(pip_version.decode('utf-8').strip())

        # Try installing a package
        subprocess.check_call(['pip', 'install', 'requests'])
        print("Requests package installed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    check_pip()
