
import sys
import os

# Add your custom directory to the PYTHONPATH
custom_path = os.path.abspath('path/to/your/source')
if custom_path not in sys.path:
    sys.path.append(custom_path)

# Now you can import modules from the custom path
import my_module  # This can be a module in the custom_path
