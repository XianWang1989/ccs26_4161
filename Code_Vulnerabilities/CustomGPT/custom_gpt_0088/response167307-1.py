
import sys
import os

# Example directories to add
src_dir = '/path/to/your/source'
test_dir = '/path/to/your/tests'

# Add directories to PYTHONPATH
sys.path.append(src_dir)
sys.path.append(test_dir)

# Now you can import modules from these directories
import your_module
