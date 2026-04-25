
import sys
import os

# Specify your source directories
source_dirs = [
    '/path/to/your/production_code',
    '/path/to/your/testing_code',
    '/path/to/your/git_submodule/packages'
]

# Add each directory to sys.path
for directory in source_dirs:
    if os.path.exists(directory):
        sys.path.append(directory)
    else:
        print(f"Warning: {directory} does not exist")

# Now you can import modules from those directories
# Example: from my_module import MyClass
