
import sys
import os

# Specify your multiple source directories
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

# Add each directory to sys.path
for dir in source_dirs:
    if os.path.exists(dir):  # Only add existing directories
        sys.path.append(dir)

# Now you can import your modules as needed
import your_module  # replace with the actual module name
