
import sys
import os

# Define your directories
directories = [
    '/path/to/production/code',
    '/path/to/testing/code',
    '/path/to/git/submodule'
]

# Add each directory to sys.path
for directory in directories:
    if os.path.exists(directory) and directory not in sys.path:
        sys.path.append(directory)

# Now you can import your modules from these directories
