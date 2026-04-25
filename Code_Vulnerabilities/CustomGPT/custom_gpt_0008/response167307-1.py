
import sys
import os

# Add directories to PYTHONPATH
sys.path.append('/path/to/your/directory1')
sys.path.append('/path/to/your/directory2')

# For example, if you have a production and testing folder:
prod_dir = os.path.abspath('/path/to/production')
test_dir = os.path.abspath('/path/to/testing')

sys.path.append(prod_dir)
sys.path.append(test_dir)

# Now you can import your modules
try:
    import your_module  # Replace with your actual module
except ImportError as e:
    print(f"Error importing module: {e}")
