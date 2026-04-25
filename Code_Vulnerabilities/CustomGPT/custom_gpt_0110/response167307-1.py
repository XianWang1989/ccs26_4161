
import sys
import os

# Add multiple directories to the PYTHONPATH
src_dirs = [
    '/path/to/production/code',  # Production code directory
    '/path/to/testing/code',     # Testing code directory
    '/path/to/git/submodule',    # Git submodule directory
]

# Add each directory to sys.path
for directory in src_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import your modules from the specified directories
# Example import
try:
    import your_module  # Replace with your actual module
except ImportError:
    print("Module not found in specified directories.")
