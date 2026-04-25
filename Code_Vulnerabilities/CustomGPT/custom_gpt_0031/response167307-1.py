
import sys
import os

# Specify your source directories
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule',
]

# Add each directory to sys.path
for directory in source_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from these directories
import your_module  # Example of importing a module

# Use your_module as needed
