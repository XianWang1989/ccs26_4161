
import sys
import os

# Add multiple directories to sys.path
# For example, adding 'src' and 'tests' directories
src_dir = os.path.join(os.path.dirname(__file__), 'src')
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

if tests_dir not in sys.path:
    sys.path.insert(0, tests_dir)

# Now you can import your modules from these directories
import my_module  # Assume my_module is in the 'src' directory
