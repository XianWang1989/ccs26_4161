
import sys
import os

# Add your custom directory to the PYTHONPATH
custom_path = '/path/to/your/directory'
if custom_path not in sys.path:
    sys.path.insert(0, custom_path)

# Now you can import modules from that directory
import my_module
