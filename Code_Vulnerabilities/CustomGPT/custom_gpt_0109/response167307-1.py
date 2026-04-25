
import sys
import os

# Add multiple directories to PYTHONPATH
directories = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

for directory in directories:
    if os.path.exists(directory):
        sys.path.append(directory)

# Now you can import modules from these directories
try:
    import your_module  # Replace with actual module name
except ImportError:
    print("Module not found in specified directories.")
