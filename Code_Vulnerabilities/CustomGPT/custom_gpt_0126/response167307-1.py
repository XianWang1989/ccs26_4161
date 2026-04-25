
import sys
import os

# Adding multiple directories to the PYTHONPATH
project_root = os.path.abspath(os.path.dirname(__file__))  # Current directory
src_directory = os.path.join(project_root, 'src')
test_directory = os.path.join(project_root, 'tests')

# Append the directories to sys.path
if src_directory not in sys.path:
    sys.path.append(src_directory)

if test_directory not in sys.path:
    sys.path.append(test_directory)

# Now you can import modules from these directories
# For example:
# from my_module import MyClass
