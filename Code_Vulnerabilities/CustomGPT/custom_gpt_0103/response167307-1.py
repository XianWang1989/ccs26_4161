
import sys
import os

# Add a directory to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'test'))

# Now you can import modules from these directories
import mymodule  # Assuming mymodule is in 'src'
