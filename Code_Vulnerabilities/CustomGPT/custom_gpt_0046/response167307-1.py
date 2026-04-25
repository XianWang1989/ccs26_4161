
import sys
import os

# Add custom directories
custom_paths = [
    '/path/to/your/source1',
    '/path/to/your/source2',
    '/path/to/testing',
]

for path in custom_paths:
    if path not in sys.path:
        sys.path.append(path)

# Now you can import your modules
import your_module  # assuming 'your_module' is located in one of the added paths
