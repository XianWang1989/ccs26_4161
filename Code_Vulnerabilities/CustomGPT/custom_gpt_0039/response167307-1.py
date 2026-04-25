
import sys
import os

# Add multiple directories to the Python path
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

for directory in source_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from the added directories
# Example: from my_module import my_function
