
import sys
import os

# Add multiple directories to sys.path
src_dir = os.path.join(os.path.dirname(__file__), 'src')
test_dir = os.path.join(os.path.dirname(__file__), 'tests')

# Ensure directories exist before adding
if os.path.exists(src_dir):
    sys.path.append(src_dir)

if os.path.exists(test_dir):
    sys.path.append(test_dir)

# Now you can import your modules
from my_module import my_function  # Assume my_module.py is in src_dir
