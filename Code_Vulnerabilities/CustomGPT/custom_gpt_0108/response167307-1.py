
import sys
import os

# Add a new directory to PYTHONPATH
new_directory = '/path/to/your/directory'
if new_directory not in sys.path:
    sys.path.append(new_directory)

# Now you can import modules from the new directory
try:
    import your_module
except ImportError:
    print("Module not found in the specified directory.")
