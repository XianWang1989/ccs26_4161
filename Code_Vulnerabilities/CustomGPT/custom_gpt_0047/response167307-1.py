
import sys
import os

# Add multiple directories to the path
source_dirs = [
    '/path/to/production_code',
    '/path/to/testing_code',
    '/path/to/git_submodule',
]

for directory in source_dirs:
    if os.path.exists(directory):
        sys.path.append(directory)

# Now you can import modules from the specified directories
import your_module  # Replace with your actual module name

# Your code logic here
