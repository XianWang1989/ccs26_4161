
import sys
import os

# Example: Add directories to PYTHONPATH
production_dir = '/path/to/production/code'
testing_dir = '/path/to/testing/code'

# Adding directories to sys.path
if production_dir not in sys.path:
    sys.path.append(production_dir)

if testing_dir not in sys.path:
    sys.path.append(testing_dir)

# Now you can import modules from these directories
try:
    import my_production_module
    import my_testing_module
except ImportError as e:
    print(f"Module not found: {e}")

# Print the current PYTHONPATH
print("Current PYTHONPATH:")
print(os.environ.get('PYTHONPATH', 'Not Set'))
print("sys.path:")
print(sys.path)
