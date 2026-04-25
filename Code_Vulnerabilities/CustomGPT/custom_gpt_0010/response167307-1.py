
import sys
import os

# Add multiple directories to the PYTHONPATH
def add_to_pythonpath(*directories):
    for directory in directories:
        if directory not in sys.path:
            sys.path.append(directory)
            print(f"Added {directory} to PYTHONPATH")

# Example usage
add_to_pythonpath('/path/to/source1', '/path/to/source2')

# Now you can import modules from the added directories
