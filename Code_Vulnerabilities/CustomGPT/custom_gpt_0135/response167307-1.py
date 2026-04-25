
import sys
import os

# Adding directories to sys.path
def add_to_path(*dirs):
    for directory in dirs:
        # Ensure it's an absolute path
        abs_path = os.path.abspath(directory)
        if abs_path not in sys.path:
            sys.path.append(abs_path)

# Example usage
add_to_path('src', 'tests', 'submodule/lib')

# Now you can import modules from these directories
# from my_module import MyClass
