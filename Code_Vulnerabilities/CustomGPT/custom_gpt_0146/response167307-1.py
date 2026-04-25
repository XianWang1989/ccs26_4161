
import sys
import os

# Define your directories
dir1 = os.path.abspath('/path/to/your/source1')
dir2 = os.path.abspath('/path/to/your/source2')

# Add the directories to sys.path
if dir1 not in sys.path:
    sys.path.append(dir1)

if dir2 not in sys.path:
    sys.path.append(dir2)

# Now you can import modules from these directories
from your_module import your_function

# Use the imported function
your_function()
