
import sys
import os

# Define the additional source directories you want to include
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    os.path.join(os.path.dirname(__file__), 'submodule/path/to/python/packages')
]

# Add each source directory to sys.path
for dir in source_dirs:
    if dir not in sys.path:
        sys.path.append(dir)

# Now you can import your modules from these directories
# For instance, if you have a module named `my_module.py` in any of the specified directories:
try:
    import my_module
except ImportError as e:
    print(f"Error importing module: {e}")

# Your other code goes here
