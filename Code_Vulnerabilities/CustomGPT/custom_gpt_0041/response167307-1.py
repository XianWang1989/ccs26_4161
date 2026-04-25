
import sys
import os

# Add directories to the Python path
sys.path.append('/path/to/your/directory')  # Production code
sys.path.append('/path/to/your/test/directory')  # Testing code

# You can also include Git submodule paths
sys.path.append(os.path.join(os.path.dirname(__file__), 'submodule_name'))

# Now you can import modules from these directories
import your_module
