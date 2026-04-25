
import sys
import os

# Add a specific directory to the PYTHONPATH
sys.path.append('/path/to/your/directory')

# If you have multiple directories, you can add them like this
additional_dirs = ['/path/to/another/directory', '/path/to/yet/another/directory']
for directory in additional_dirs:
    if os.path.exists(directory):
        sys.path.append(directory)

# Now you can import your modules from the added directories
import your_module  # Make sure 'your_module' is located in one of the added directories
