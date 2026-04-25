
import sys
import os

# Append your directories to sys.path
production_path = os.path.abspath('./production')
testing_path = os.path.abspath('./testing')

# Add the paths
if production_path not in sys.path:
    sys.path.append(production_path)
if testing_path not in sys.path:
    sys.path.append(testing_path)

# Now you can import modules from these directories
import your_module  # Replace with your actual module name
