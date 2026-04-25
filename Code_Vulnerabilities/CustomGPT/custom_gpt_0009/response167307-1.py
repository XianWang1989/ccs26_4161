
import sys
import os

# Add a directory to the PYTHONPATH
directory = '/path/to/your/source'
if directory not in sys.path:
    sys.path.append(directory)

# Now you can import your modules
import your_module

# Example of accessing a module from a testing directory
test_directory = '/path/to/your/test/source'
if test_directory not in sys.path:
    sys.path.append(test_directory)

# Import your test module
import your_test_module
