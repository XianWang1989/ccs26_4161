
import sys
import os

# Add multiple directories to the PYTHONPATH
source_dirs = [
    '/path/to/your/production_code',
    '/path/to/your/testing_code',
    '/path/to/your/git_submodule/packages'
]

# Add each directory to sys.path
for directory in source_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from these directories
try:
    import my_module  # An example module you expect in the added directories
except ImportError:
    print("Module not found in the specified directories.")
