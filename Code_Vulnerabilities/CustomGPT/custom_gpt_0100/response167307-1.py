
import sys
import os

# Add multiple directories to PYTHONPATH
directories = [
    '/path/to/your/source1',
    '/path/to/your/source2',
    '/path/to/your/testing'
]

for directory in directories:
    if os.path.exists(directory):
        sys.path.append(directory)

# Now you can import modules from the added directories
