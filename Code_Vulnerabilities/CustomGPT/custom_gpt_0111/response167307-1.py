
import sys
import os

# Define your source directories
source_dirs = [
    '/path/to/production/code',
    '/path/to/testing/code',
    # If using a Git submodule
    '/path/to/git/submodule',
]

# Add each directory to sys.path
for directory in source_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from these directories
import my_module  # This module can be in any of the specified directories
