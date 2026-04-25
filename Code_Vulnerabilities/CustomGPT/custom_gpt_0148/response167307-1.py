
import sys
import os

# Define your source directories
source_directories = [
    os.path.abspath('src'),           # Relative path to your source
    os.path.abspath('tests'),         # Directory for tests
    os.path.abspath('libs'),          # Git submodule or third-party libs
]

# Add directories to PYTHONPATH
for directory in source_directories:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import your modules from the specified directories
from my_module import my_function

# Example usage
my_function()
