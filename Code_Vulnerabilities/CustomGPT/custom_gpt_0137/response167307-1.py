
import sys
import os

# Adding multiple directories to the PYTHONPATH
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

# Adding each directory to sys.path
for directory in source_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import your modules as needed
try:
    import your_module  # Replace 'your_module' with the actual module name
except ImportError:
    print("Module not found. Ensure the directories are correct.")
