
import sys
import os

# Add multiple directories to sys.path
sys.path.append('/path/to/dir1')
sys.path.append('/path/to/dir2')

# Alternatively, for dynamic addition based on the environment
if 'MY_DEV_ENV' in os.environ:
    sys.path.append('/path/to/development')
else:
    sys.path.append('/path/to/production')

# Now you can import modules from the added paths
import my_module  # Example module located in the specified directories
