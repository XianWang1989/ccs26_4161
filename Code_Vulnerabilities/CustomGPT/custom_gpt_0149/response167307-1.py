
import sys
import os

# Add multiple directories to sys.path
src_paths = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

# Append each path to sys.path
for path in src_paths:
    if path not in sys.path:
        sys.path.append(path)

# Now you can import modules from the specified directories
import your_module  # Replace with your actual module
