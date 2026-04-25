
import sys
import os

# Assume you have multiple directories for your source code
project_root = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(project_root, 'src')
test_dir = os.path.join(project_root, 'tests')

# Add source and test directories to sys.path
sys.path.append(src_dir)
sys.path.append(test_dir)

# Now you can import modules from these directories
from mymodule import MyClass  # from src/mymodule.py
