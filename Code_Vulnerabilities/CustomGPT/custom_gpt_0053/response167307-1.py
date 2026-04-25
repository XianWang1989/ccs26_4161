
import sys
import os

# Define your source directories
source_dirs = [
    '/path/to/production/code',
    '/path/to/testing/code',
    '/path/to/git/submodule/packages'
]

# Add each directory to the sys.path
for directory in source_dirs:
    if os.path.isdir(directory):  # Check if the directory exists
        sys.path.append(directory)

# Example of importing from the newly added directories
# Assume there's a module named 'my_module' in one of the specified directories
try:
    from my_module import SomeClass
except ImportError:
    print("Module not found in specified directories.")

# Now you can use SomeClass as needed
