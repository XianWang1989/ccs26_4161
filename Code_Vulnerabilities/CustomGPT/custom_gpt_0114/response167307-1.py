
import sys
import os

# Add directories to PYTHONPATH
src_directory = '/path/to/your/src'
test_directory = '/path/to/your/tests'

# Append the directories to sys.path
if src_directory not in sys.path:
    sys.path.append(src_directory)

if test_directory not in sys.path:
    sys.path.append(test_directory)

# Now you can import modules from these directories
import your_module  # Assuming 'your_module.py' is in src_directory
