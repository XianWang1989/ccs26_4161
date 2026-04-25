
import sys
import os

# List of directories to add
source_dirs = [
    'path/to/production',
    'path/to/testing',
    'path/to/git/submodule'
]

for source_dir in source_dirs:
    abs_path = os.path.abspath(source_dir)
    if abs_path not in sys.path:
        sys.path.append(abs_path)

# Import your modules
import production_module
import testing_module
import submodule_package
