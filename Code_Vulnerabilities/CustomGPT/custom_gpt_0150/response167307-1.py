
import sys
import os

# Option 1: Modify PYTHONPATH in the script
def add_to_pythonpath(path):
    if path not in sys.path:
        sys.path.append(path)

# Add your source directories
add_to_pythonpath('path/to/your/production')
add_to_pythonpath('path/to/your/testing')

# Option 2: Set PYTHONPATH before running your script
# This can be done in the terminal:
# export PYTHONPATH=/path/to/your/production:/path/to/your/testing:$PYTHONPATH
