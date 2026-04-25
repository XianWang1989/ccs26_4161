
import sys
import os

# Define your custom paths
custom_paths = [
    '/path/to/production/source',
    '/path/to/testing/source',
    '/path/to/git/submodule'
]

# Add the custom paths to sys.path
for path in custom_paths:
    if os.path.isdir(path):  # Check if the path exists
        sys.path.append(path)

# Now you can import modules from these directories
try:
    import my_module  # Replace with your actual module
    print("Module imported successfully!")
except ImportError as e:
    print(f"Error importing module: {e}")
