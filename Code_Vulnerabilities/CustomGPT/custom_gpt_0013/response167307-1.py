
import sys
import os

# Add custom directories
sys.path.append('/path/to/your/source1')
sys.path.append('/path/to/your/source2')

# Example usage: Importing a module from the added path
try:
    import my_module
except ImportError as e:
    print(f"Error importing module: {e}")
