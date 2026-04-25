
import sys
import os

# Define your directories
production_dir = "/path/to/production"
testing_dir = "/path/to/testing"

# Add directories to sys.path
sys.path.append(production_dir)
sys.path.append(testing_dir)

# Now you can import modules from these directories
import your_module  # Ensure this module exists in one of the added paths
