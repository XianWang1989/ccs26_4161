
import sys
import os

# Add multiple directories to sys.path
source_dirs = [
    '/path/to/production/code',
    '/path/to/testing/code',
    '/path/to/git/submodule'
]

# Append each directory to sys.path
for dir in source_dirs:
    if os.path.isdir(dir):  # Check if the directory exists
        sys.path.append(dir)

# Now you can import modules from these directories
try:
    import my_module  # Replace with your actual module
except ImportError:
    print("Module not found in the specified directories.")
