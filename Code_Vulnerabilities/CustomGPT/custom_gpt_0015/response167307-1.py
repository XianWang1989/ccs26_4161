
import sys
import os

# Dynamically add directories to the Python path
current_directory = os.path.dirname(os.path.abspath(__file__))

# Example: Adding multiple directories
source_directories = [
    os.path.join(current_directory, 'src'),
    os.path.join(current_directory, 'lib'),
    os.path.join(current_directory, 'tests')
]

# Adding to sys.path
for directory in source_directories:
    if directory not in sys.path:
        sys.path.append(directory)

# Now you can import your modules from the added directories
try:
    import my_module  # Replace with your actual module name
except ImportError:
    print("Module not found in specified paths.")
