
import sys
import os

# Define your source directories
source_dirs = [
    '/path/to/your/production_code',
    '/path/to/your/testing_code',
    '/path/to/your/git_submodule'
]

# Add each source directory to the sys.path
for directory in source_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from these directories
# Example: from my_module import MyClass
