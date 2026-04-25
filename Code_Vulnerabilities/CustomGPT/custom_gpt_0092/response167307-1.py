
import sys
import os

# Define your custom paths
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule/package'
]

# Add each source directory to sys.path
for directory in source_dirs:
    if os.path.exists(directory):
        sys.path.append(directory)

# Now you can import modules from the specified directories
