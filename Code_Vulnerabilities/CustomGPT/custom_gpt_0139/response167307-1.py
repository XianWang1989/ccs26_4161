
import sys
import os

# Add custom directories to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory
src_dir = os.path.join(current_dir, 'src')  # Custom source directory
test_dir = os.path.join(current_dir, 'tests')  # Test source directory

# Adding directories to sys.path
sys.path.append(src_dir)
sys.path.append(test_dir)

# Now you can import your modules from these directories
from my_module import my_function  # Example import
