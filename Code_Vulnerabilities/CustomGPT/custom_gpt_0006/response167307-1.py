
import sys
import os

# Add a directory to PYTHONPATH
new_path = "/path/to/your/directory"
if new_path not in sys.path:
    sys.path.append(new_path)

# Now you can import modules from that directory
import your_module
