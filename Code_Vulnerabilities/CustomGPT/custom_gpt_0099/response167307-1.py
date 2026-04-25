
import sys
import os

# Specify directories you want to add
additional_paths = [
    '/path/to/your/first/source',
    '/path/to/your/second/source'
]

# Add each directory to sys.path
for path in additional_paths:
    if os.path.exists(path):
        sys.path.append(path)

# Now you can import modules from these directories
import your_module
