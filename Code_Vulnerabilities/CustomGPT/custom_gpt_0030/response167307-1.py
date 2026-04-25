
import sys
import os

# Add multiple directories to sys.path
# Example directories
source_dirs = [
    '/path/to/production_code',
    '/path/to/testing_code',
    '/path/to/git_submodule/python_packages'
]

for dir in source_dirs:
    if os.path.exists(dir) and dir not in sys.path:
        sys.path.append(dir)

# Now you can import modules from these directories
