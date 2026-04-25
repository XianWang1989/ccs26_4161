
import subprocess

# Replace 'your_package' with the actual package name you want to install
package_name = 'your_package'

try:
    subprocess.check_call(['pip', 'install', package_name])
    print(f'Successfully installed {package_name}')
except subprocess.CalledProcessError as e:
    print(f'Error installing package: {e}')
