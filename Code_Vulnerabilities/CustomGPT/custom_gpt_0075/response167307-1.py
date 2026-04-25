
import sys
import os

# Add directories to the path as needed
sys.path.append('/path/to/my_module')
sys.path.append('/path/to/another_module')

# Example usage
try:
    import my_module  # Attempt to import
except ImportError as e:
    print(f"Import Error: {e}")

# Confirm the paths
print(sys.path)
