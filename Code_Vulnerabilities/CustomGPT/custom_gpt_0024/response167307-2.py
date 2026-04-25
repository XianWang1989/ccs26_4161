
import sys
import os

# Define directories you want to include
directories = ['/path/to/production_code', '/path/to/testing_code']

# Add each directory to sys.path
for directory in directories:
    if directory not in sys.path:
        sys.path.append(directory)

# Print current sys.path
print("Updated PYTHONPATH:")
for path in sys.path:
    print(path)
