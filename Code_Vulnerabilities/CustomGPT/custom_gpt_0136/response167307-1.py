
import sys
import os

# Add directories to sys.path
# Replace these with your actual directories
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

# Add each directory to sys.path
for directory in source_dirs:
    if os.path.isdir(directory):  # Check if the directory exists
        sys.path.append(directory)

# Now, you can import modules from the specified directories
try:
    import your_module  # Replace with your actual module name
except ImportError:
    print("Module not found.")
