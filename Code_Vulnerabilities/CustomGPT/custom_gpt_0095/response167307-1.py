
import sys
import os

# Adding multiple directories to sys.path
source_dirs = [
    'path/to/your/source1',
    'path/to/your/source2',
    'path/to/your/test',
]

# Adding each directory to sys.path
for dir in source_dirs:
    if os.path.exists(dir) and dir not in sys.path:
        sys.path.append(dir)

# Now you can import modules from these directories
import your_module  # Replace with your actual module
