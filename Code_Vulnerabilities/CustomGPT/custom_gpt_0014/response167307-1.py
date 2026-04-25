
import sys
import os

# Define your additional directories
additional_dirs = [
    '/path/to/your/source1',
    '/path/to/your/source2',
    '/path/to/your/test_source',
]

# Add each directory to sys.path
for directory in additional_dirs:
    if os.path.exists(directory):
        sys.path.append(directory)

# Verify the directories are added
print("Current PYTHONPATH:")
print("\n".join(sys.path))
