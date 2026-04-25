
import sys
import os

# Example directories
src_dir = os.path.join(os.path.dirname(__file__), 'src')
test_dir = os.path.join(os.path.dirname(__file__), 'tests')
lib_dir = os.path.join(os.path.dirname(__file__), 'lib')

# Insert the directories into PYTHONPATH
sys.path.insert(0, src_dir)  # Add src directory first
sys.path.insert(1, test_dir)  # Add tests directory
sys.path.insert(2, lib_dir)   # Add lib directory

# Now you can import modules from these directories
# Example:
# from my_module import MyClass
