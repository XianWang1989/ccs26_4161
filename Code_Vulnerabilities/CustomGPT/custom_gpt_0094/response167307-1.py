
import sys
import os

# Add your source directories
source_dir_1 = '/path/to/your/source1'
source_dir_2 = '/path/to/your/source2'
source_dir_3 = '/path/to/your/testing'

# Update PYTHONPATH
sys.path.append(source_dir_1)
sys.path.append(source_dir_2)
sys.path.append(source_dir_3)

# Now you can import modules from these directories
import your_module  # Replace with your actual module

# Example usage of your_module
your_module.some_function()
