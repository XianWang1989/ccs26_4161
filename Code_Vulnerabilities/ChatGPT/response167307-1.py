
import sys
import os

# Specify the directories you want to include
additional_dirs = ['/path/to/dir1', '/path/to/dir2']

# Add each directory to sys.path
for directory in additional_dirs:
    if os.path.exists(directory):
        sys.path.append(directory)

# Now you can import modules from the specified directories
# Your imports here, for example:
# from mymodule import myfunction
