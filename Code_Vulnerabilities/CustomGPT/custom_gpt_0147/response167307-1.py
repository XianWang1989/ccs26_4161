
import sys
import os

# Add a single directory to PYTHONPATH
sys.path.append('/path/to/your/directory')

# You can also add multiple directories
additional_dirs = ['/path/to/another/directory', '/path/to/yet/another/directory']
sys.path.extend(additional_dirs)

# Verify the current PYTHONPATH
print("Current PYTHONPATH:")
for path in sys.path:
    print(path)

# Now you can import your modules
import your_module  # Replace with your actual module
