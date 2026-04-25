
import sys
import os

# Add your directories here
directories = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

# Add each directory to PYTHONPATH
for directory in directories:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from these directories
import your_module  # Replace with your actual module name
