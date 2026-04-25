
import sys
import os

# Add a specific directory to the Python path
# Example: Adding a directory named 'my_module_directory' located in the current working directory
current_directory = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
my_module_directory = os.path.join(current_directory, 'my_module_directory')  # Construct the path

# Insert the directory at the front of sys.path
if my_module_directory not in sys.path:
    sys.path.insert(0, my_module_directory)

# Now you can import modules from 'my_module_directory'
import my_module  # Assuming there is a my_module.py file in 'my_module_directory'
