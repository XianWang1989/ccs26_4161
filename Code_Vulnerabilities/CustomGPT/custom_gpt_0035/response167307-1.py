
import sys
import os

# Define your source directories
source_dirs = [
    '/path/to/production',
    '/path/to/testing',
    '/path/to/git/submodule'
]

# Add them to sys.path
for dir in source_dirs:
    if os.path.exists(dir):
        sys.path.append(dir)

# Now you can import modules from those directories
