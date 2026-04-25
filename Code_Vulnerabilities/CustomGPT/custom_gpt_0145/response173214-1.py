
# Example of setting up a virtual environment and installing a package
import os
import subprocess
import sys

# Create a virtual environment
subprocess.check_call([sys.executable, '-m', 'venv', 'myenv'])

# Activate the environment
activate_script = os.path.join('myenv', 'Scripts', 'activate_this.py')
with open(activate_script) as file_:
    exec(file_.read(), dict(__file__=activate_script))

# Install a package using pip
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'your-package-name'])
