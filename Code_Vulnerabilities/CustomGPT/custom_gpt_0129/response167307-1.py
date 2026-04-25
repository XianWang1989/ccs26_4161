
import sys
import os

# Add directories to sys.path
# Example directories
source_dir_1 = '/path/to/your/source/directory1'
source_dir_2 = '/path/to/your/source/directory2'

# Dynamically add the directories to sys.path
sys.path.append(source_dir_1)
sys.path.append(source_dir_2)

# Now you can import modules from these directories
try:
    import my_module  # This module should be in one of the specified directories
except ImportError:
    print("Module not found.")
