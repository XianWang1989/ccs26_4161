
import sys
import os

# Add multiple directories to sys.path
src_dir = '/path/to/your/source'
test_dir = '/path/to/your/testing'
submodule_dir = '/path/to/your/git/submodule'

# Append the directories to sys.path
sys.path.append(src_dir)
sys.path.append(test_dir)
sys.path.append(submodule_dir)

# Now you can import modules from these directories
import your_module  # Replace with your actual module name
