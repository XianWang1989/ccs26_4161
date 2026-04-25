
import sys
import os

# Add additional directories to sys.path
sys.path.append('/path/to/your/source1')
sys.path.append('/path/to/your/source2')

# Optionally, you can also set the PYTHONPATH from within the script
os.environ['PYTHONPATH'] = '/path/to/your/source1:/path/to/your/source2'

# Now you can import your modules as needed
import your_module  # Replace with your actual module name
