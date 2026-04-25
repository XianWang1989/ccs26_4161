
import sys
import os

# Add a single directory to PYTHONPATH
sys.path.append('/path/to/your/directory')

# Add multiple directories
additional_paths = [
    '/path/to/production',
    '/path/to/testing'
]

for path in additional_paths:
    if os.path.exists(path):
        sys.path.append(path)

# Now you can import your modules
import your_module  # Make sure the module is in one of the added directories
