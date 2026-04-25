
import sys
import os

# Add a custom directory to PYTHONPATH
new_dir = os.path.abspath('path/to/your/module')
if new_dir not in sys.path:
    sys.path.append(new_dir)

# Now you can import your module
import your_module
