
import os
import subprocess

# Path to your Visual Studio installation
vs_path = r"C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build"
vcvarsall_path = os.path.join(vs_path, 'vcvarsall.bat')

# Check if vcvarsall.bat exists
if os.path.exists(vcvarsall_path):
    # Run vcvarsall.bat to set up the environment
    subprocess.call([vcvarsall_path, 'x64'])

    # Now you can use pip
    subprocess.call(['pip', 'install', 'your-package-name'])
else:
    print("vcvarsall.bat not found. Ensure Visual C++ Build Tools are installed.")
