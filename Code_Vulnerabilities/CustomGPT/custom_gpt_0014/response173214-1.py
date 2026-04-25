
import subprocess
import sys

# Replace 'package_name' with your desired package
package_name = 'requests'

# Installing the package
subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
