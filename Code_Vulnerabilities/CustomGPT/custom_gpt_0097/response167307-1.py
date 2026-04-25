
import sys
import os

# Define your paths
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

# Add paths to PYTHONPATH
for dir in source_dirs:
    if os.path.isdir(dir) and dir not in sys.path:
        sys.path.append(dir)

# Now you can import your modules from the specified directories
import your_module
