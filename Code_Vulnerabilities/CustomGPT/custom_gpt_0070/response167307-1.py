
import sys
import os

# Add custom directories to PYTHONPATH
custom_paths = [
    "path/to/your/production/code",
    "path/to/your/testing/code",
    "path/to/your/git/submodule"
]

# Append each path to sys.path
for path in custom_paths:
    if os.path.exists(path):
        sys.path.append(path)

# Now you can import modules from the added paths
# Example: from your_module import your_function
