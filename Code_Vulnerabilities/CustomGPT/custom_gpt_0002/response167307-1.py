
import sys
import os

# Add multiple source directories to PYTHONPATH
source_dirs = [
    'path/to/production_code',
    'path/to/testing_code',
    'path/to/git_submodule',
]

for dir in source_dirs:
    if os.path.exists(dir):
        sys.path.append(dir)

# Now you can import your modules from the added directories
import your_module
