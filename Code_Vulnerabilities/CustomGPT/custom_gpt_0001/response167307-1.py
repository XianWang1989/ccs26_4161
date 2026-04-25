
import sys
import os

# Add multiple directories to sys.path
source_dirs = [
    '/path/to/your/first/source/directory',
    '/path/to/your/second/source/directory',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

for dir in source_dirs:
    if os.path.isdir(dir):
        sys.path.append(dir)

# Now you can import modules from these directories
import my_module  # Example: this will import from the added directories
