
import sys
import os

# Add your custom directories
custom_dir1 = '/path/to/your/custom/dir1'
custom_dir2 = '/path/to/your/custom/dir2'

# Add the directories to the sys.path
sys.path.append(custom_dir1)
sys.path.append(custom_dir2)

# Now you can import modules from those directories
try:
    import your_module  # replace with your actual module
except ImportError:
    print("Module not found in specified directories.")
