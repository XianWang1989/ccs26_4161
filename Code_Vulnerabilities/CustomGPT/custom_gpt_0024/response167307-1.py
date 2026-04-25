
import sys
import os

# Add multiple directories to sys.path
sys.path.append('/path/to/dir1')
sys.path.append('/path/to/dir2')

# Optionally, you can print the current PYTHONPATH for verification
print("Current PYTHONPATH:", os.environ.get('PYTHONPATH', ''))
