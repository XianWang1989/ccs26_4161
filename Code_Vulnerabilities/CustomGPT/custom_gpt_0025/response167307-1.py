
import sys
import os

# Add custom directories to PYTHONPATH
additional_paths = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule'
]

for path in additional_paths:
    if os.path.exists(path):
        sys.path.append(path)

# Now you can import your modules
from your_module import YourClass
