
import sys
import os

# Add multiple directories to sys.path
source_dirs = [
    '/path/to/your/production/code',
    '/path/to/your/testing/code',
    '/path/to/your/git/submodule/packages'
]

for dir in source_dirs:
    if os.path.exists(dir) and dir not in sys.path:
        sys.path.append(dir)

# Now you can import modules from the specified directories
try:
    import your_module  # Replace with actual module
except ImportError:
    print("Module not found in specified directories.")
