import sys
import os

# Add a relative path to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Now you can import modules from the added path
from mymodule import myfunction
