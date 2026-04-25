
import sys
import os

# Add directories to the Python path
src_dir = os.path.abspath("path/to/your/source/directory")
test_dir = os.path.abspath("path/to/your/test/directory")

if src_dir not in sys.path:
    sys.path.append(src_dir)

if test_dir not in sys.path:
    sys.path.append(test_dir)

# Now you can import modules from these directories
import my_module
