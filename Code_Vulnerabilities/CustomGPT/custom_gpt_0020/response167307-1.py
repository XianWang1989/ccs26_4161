
import sys
import os

# Adding a new directory to PYTHONPATH
new_path = '/path/to/your/directory'
if new_path not in sys.path:
    sys.path.append(new_path)

# Now you can import your module from the newly added path
import your_module  # Replace with your actual module name
