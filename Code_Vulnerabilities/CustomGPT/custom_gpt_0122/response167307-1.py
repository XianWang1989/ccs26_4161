
import sys
import os

# Set your directory paths
production_path = os.path.abspath('/path/to/production')
testing_path = os.path.abspath('/path/to/testing')

# Add the paths to sys.path
sys.path.append(production_path)
sys.path.append(testing_path)

# Now you can import modules from these directories
