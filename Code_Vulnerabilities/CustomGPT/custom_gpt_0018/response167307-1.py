
import sys
import os

# Add a directory to the Python path
additional_path = '/path/to/your/directory'
if additional_path not in sys.path:
    sys.path.append(additional_path)

# Now you can import your module
import my_module  # Replace with your actual module name
