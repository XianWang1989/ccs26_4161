
import sys
import os

# Adding a directory to PYTHONPATH
new_path = '/path/to/your/directory'
if new_path not in sys.path:
    sys.path.append(new_path)

# Now you can import modules from the above directory
import your_module
