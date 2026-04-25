
import sys
import os

# Assume you have multiple directories for production and testing code.
prod_dir = '/path/to/your/production_code'
test_dir = '/path/to/your/testing_code'

# Append the directories to sys.path
if os.path.exists(prod_dir):
    sys.path.append(prod_dir)

if os.path.exists(test_dir):
    sys.path.append(test_dir)

# Example of importing a module from the specified directories
try:
    import your_module_from_production  # This will now work if the directory is correctly added
    print("Production module imported successfully!")

    import your_module_from_testing  # This will also work if the testing directory is added
    print("Testing module imported successfully!")
except ImportError as e:
    print(f"ImportError: {e}")
