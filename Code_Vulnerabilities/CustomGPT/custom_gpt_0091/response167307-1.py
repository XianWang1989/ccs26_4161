
import sys
import os

# Define your multiple source directories
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

# Add directories to PYTHONPATH
for dir in source_dirs:
    if os.path.isdir(dir):  # Check if the directory exists
        sys.path.append(dir)

# Now you can import your modules from these directories
# e.g., from my_module import MyClass
