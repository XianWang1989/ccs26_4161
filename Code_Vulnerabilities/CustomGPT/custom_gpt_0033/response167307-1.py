
import sys
import os

# Adding multiple directories to sys.path
source_dirs = [
    '/path/to/production/code',
    '/path/to/testing/code',
    '/path/to/git/submodule',
]

# Adding each directory to sys.path
for dir in source_dirs:
    if os.path.isdir(dir):  # Check if the directory exists
        sys.path.append(dir)

# Now you can import modules from the specified directories
import my_module  # Replace with your module
