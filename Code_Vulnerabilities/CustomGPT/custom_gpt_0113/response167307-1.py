
import sys
import os

# Add custom directories to PYTHONPATH
sys.path.append('/path/to/your/source/directory1')
sys.path.append('/path/to/your/source/directory2')

# If using a Git submodule
sys.path.append(os.path.join(os.path.dirname(__file__), 'submodule_directory'))

# Now you can import your modules
import your_module
