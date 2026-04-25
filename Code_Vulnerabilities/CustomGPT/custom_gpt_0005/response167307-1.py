
import sys
import os

# Add directories to the PYTHONPATH
def add_to_path(*directories):
    for directory in directories:
        if os.path.isdir(directory):
            sys.path.append(directory)
        else:
            print(f"Directory {directory} does not exist.")

# Example usage
add_to_path('/path/to/production', '/path/to/testing', '/path/to/git/submodule')

# Now you can import modules from the specified directories
# For example:
# from my_module import my_function
