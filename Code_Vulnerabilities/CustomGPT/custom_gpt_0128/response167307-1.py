
import sys
import os

# Add a directory to the Python path
new_path = '/path/to/your/directory'
if new_path not in sys.path:
    sys.path.append(new_path)

# You can also add multiple directories
additional_paths = [
    '/path/to/another/directory',
    '/path/to/testing/directory'
]
for path in additional_paths:
    if path not in sys.path:
        sys.path.append(path)

# Now you can import your modules from these directories
import your_module

# Verify the current PYTHONPATH
print("Current PYTHONPATH:", sys.path)
