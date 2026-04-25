
import sys
import os

# Add multiple directories to PYTHONPATH
source_dirs = [
    '/path/to/production/code',
    '/path/to/testing/code',
    '/path/to/git/submodule'
]

# Add directories to the sys.path
for dir in source_dirs:
    if os.path.exists(dir):
        sys.path.append(dir)

# Now you can import modules from those directories
import my_module  # Replace with your actual module
