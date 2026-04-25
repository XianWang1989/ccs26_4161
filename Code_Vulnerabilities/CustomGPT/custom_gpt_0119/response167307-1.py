
import sys
import os

# Add multiple source directories
source_dirs = [
    '/path/to/your/source1',
    '/path/to/your/source2',
    '/path/to/your/testing',
    '/path/to/your/git_submodule'
]

# Adding directories to sys.path
for dir in source_dirs:
    if dir not in sys.path:
        sys.path.append(dir)

# Now you can import modules from these directories
# For example, if you have a module named 'mymodule' in one of the directories:
try:
    import mymodule
    # Use the imported module
except ImportError:
    print("Module not found in the specified paths.")
