
import sys
import os

# Add specific directories
sys.path.append('/path/to/your/source')
sys.path.append('/path/to/your/tests')

# If you have a Git submodule
sys.path.append(os.path.join(os.path.dirname(__file__), 'submodule_directory'))

# Now you can import from these directories
import your_module
