
import sys
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add source and test directories
sys.path.append(os.path.join(current_dir, 'src'))
sys.path.append(os.path.join(current_dir, 'tests'))

# Now you can import your modules
from module1 import some_function
from test_module1 import test_some_function
