
import sys
import os

# Add your directories to the sys.path list
sys.path.append('/path/to/your/source/directory')
sys.path.append('/another/path/to/your/source/directory')

# Optionally, you can also append or set PYTHONPATH from an environment variable
os.environ['PYTHONPATH'] = '/path/to/your/source/directory:/another/path/to/your/source/directory'

# Now you can import your modules from those directories
import your_module
