
import sys
import os

# Add custom directories to the Python path
custom_dirs = [
    '/path/to/production/code',
    '/path/to/testing/code',
    '/path/to/git/submodule'
]

for directory in custom_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from the added directories
try:
    import your_module  # Replace with the actual module name
except ImportError:
    print("Module not found in the specified directories.")
