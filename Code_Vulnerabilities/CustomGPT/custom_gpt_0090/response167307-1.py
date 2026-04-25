
import sys
import os

# Add multiple source directories
source_dirs = [
    '/path/to/production',
    '/path/to/testing',
    '/path/to/git/submodule'
]

# Append directories to the system path
for dir in source_dirs:
    if os.path.exists(dir):
        sys.path.append(dir)

# Now you can import modules from the specified directories
