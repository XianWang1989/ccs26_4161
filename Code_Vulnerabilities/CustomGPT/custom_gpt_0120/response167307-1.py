
import sys
import os

# Add a directory to the PYTHONPATH at runtime
sys.path.append('/path/to/your/directory')

# Now you can import modules from this directory
import your_module

# Alternatively, set up multiple paths
source_dirs = [
    '/path/to/production/code',
    '/path/to/testing/code',
    '/path/to/submodule/src'
]

for dir in source_dirs:
    if dir not in sys.path:
        sys.path.append(dir)

# Now you can import from any of these directories
