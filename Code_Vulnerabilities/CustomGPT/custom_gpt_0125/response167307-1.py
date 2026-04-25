
import sys
import os

# Add multiple directories to sys.path
base_dir = '/path/to/your/project'
test_dir = '/path/to/your/tests'
submodule_dir = '/path/to/your/submodule'

# Setting the PYTHONPATH temporarily
sys.path.append(base_dir)
sys.path.append(test_dir)
sys.path.append(submodule_dir)

# Now you can import modules from these directories
from your_module import your_function

# Call your function
your_function()
