
import sys
import os

# Specify your source directories
source_directories = [
    '/path/to/production_code',
    '/path/to/testing_code',
    '/path/to/git_submodule'
]

# Add each directory to sys.path
for directory in source_directories:
    if os.path.exists(directory):
        sys.path.append(directory)

# Now you can import your modules
import your_module
