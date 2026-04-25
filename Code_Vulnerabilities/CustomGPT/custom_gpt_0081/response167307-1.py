
import sys
import os

# You can append directories to sys.path
sys.path.append('/path/to/your/modules')  # Adding a single directory
sys.path.append('/path/to/another/module')

# Alternatively, you can set a custom directory structure
source_dirs = [
    '/path/to/production_code',
    '/path/to/testing_code',
    '/path/to/git_submodule'
]

for directory in source_dirs:
    if directory not in sys.path:  # Ensure it's not already in the path
        sys.path.append(directory)

# Now you can import your modules from specified directories
import your_module
