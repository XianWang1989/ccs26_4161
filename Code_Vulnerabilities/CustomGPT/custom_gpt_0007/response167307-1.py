
import sys
import os

# Add multiple directories to the PYTHONPATH
source_dirs = [
    '/path/to/production/code',
    '/path/to/testing/code',
    '/path/to/git/submodule'
]

# Extend sys.path with the new directories
for directory in source_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from those directories
try:
    import my_module  # Replace with your actual module name
except ImportError:
    print("Module not found in the specified directories.")
