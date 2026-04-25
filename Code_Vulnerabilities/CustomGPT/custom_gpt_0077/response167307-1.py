
import sys
import os

# Adding multiple directories to PYTHONPATH
source_dirs = [
    "/path/to/production_code",
    "/path/to/testing_code",
    "/path/to/git_submodule"
]

# Append each directory to sys.path
for directory in source_dirs:
    if os.path.exists(directory):
        sys.path.append(directory)

# Now you can import modules from the specified directories
# Example: from mymodule import MyClass
