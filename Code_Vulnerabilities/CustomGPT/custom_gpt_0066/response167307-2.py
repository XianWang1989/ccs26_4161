
import sys
import os

# List of paths to include
paths = [
    '/path/to/production',
    '/path/to/testing',
    '/path/to/submodule'
]

# Add each path to sys.path
for path in paths:
    if path not in sys.path:
        sys.path.append(path)

# Now you can import modules from any specified directory
import production_module
import testing_module
