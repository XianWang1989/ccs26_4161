
import sys
import os

# Get the current working directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Example directories to add
additional_dirs = [
    os.path.join(current_directory, 'src'),        # Your source directory
    os.path.join(current_directory, 'lib'),        # Another directory for libraries
    '/path/to/other/directory'                      # An absolute path
]

# Add those directories to the sys.path
for directory in additional_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import modules from these new paths
# import my_module  # Example import from the added directory
