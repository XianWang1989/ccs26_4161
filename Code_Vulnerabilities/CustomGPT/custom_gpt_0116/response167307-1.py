
import sys
import os

# Specify your custom directories
source_dirs = [
    '/path/to/your/project',  # Production code
    '/path/to/testing',       # Testing code
    '/path/to/git/submodule'  # Git submodule
]

# Add directories to sys.path
for directory in source_dirs:
    if directory not in sys.path:
        sys.path.append(directory)

# Verify the changes
print("Current PYTHONPATH:")
print(os.pathsep.join(sys.path))  # Print the updated PYTHONPATH

# Now you can import your modules
# from your_module import YourClass
