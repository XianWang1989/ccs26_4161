
import sys
import os

# Add directories to sys.path dynamically
project_root = os.path.dirname(os.path.abspath(__file__))  # current directory
src_dir = os.path.join(project_root, 'src')  # adjust based on your structure
tests_dir = os.path.join(project_root, 'tests')

# Append directories to sys.path
if src_dir not in sys.path:
    sys.path.append(src_dir)

if tests_dir not in sys.path:
    sys.path.append(tests_dir)

# Now you can import modules from these directories
try:
    from my_module import MyClass  # Replace with your actual module
except ImportError:
    print("Module not found in specified directories.")
