
import sys
import os

# Adjust the PYTHONPATH
new_path = '/path/to/your/directory'
if new_path not in sys.path:
    sys.path.append(new_path)

# Now you can import your modules
import my_module
