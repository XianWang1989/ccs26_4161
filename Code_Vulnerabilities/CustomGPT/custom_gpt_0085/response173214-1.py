
import os

# Example of setting environment variables in Python
os.environ['PATH'] += r";C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build"
os.environ['VSINSTALLDIR'] = r"C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools"

# Trying to install a package
import subprocess

subprocess.run(['pip', 'install', 'requests'])
