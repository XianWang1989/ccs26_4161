
import sys
import os

# Add multiple source directories
source_dirs = [
    '/path/to/your/source1',
    '/path/to/your/source2',
    '/path/to/your/test/source',
]

# Extend sys.path with these directories
for dir in source_dirs:
    if dir not in sys.path:
        sys.path.append(dir)

# Now you can import modules from these directories
# Example import (assuming you have a module in one of these paths)
# from module_in_source1 import SomeClass
