
import sys
import os

# Example directories
prod_dir = '/path/to/production/code'
test_dir = '/path/to/testing/code'
submodule_dir = '/path/to/git/submodule'

# Add production directory
if prod_dir not in sys.path:
    sys.path.append(prod_dir)

# Add testing directory
if test_dir not in sys.path:
    sys.path.append(test_dir)

# Add Git submodule directory
if submodule_dir not in sys.path:
    sys.path.append(submodule_dir)

# Now you can import modules from these directories
try:
    import my_module  # This could be in any of the directories added above
except ImportError:
    print("Module not found! Make sure the paths are correct.")

# Print the current sys.path for debugging purposes
print("Current PYTHONPATH:", sys.path)
