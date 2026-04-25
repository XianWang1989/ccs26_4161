
import sys

# Add multiple directories to sys.path
sys.path.append('/path/to/your/first/source')
sys.path.append('/path/to/your/second/source')

# You can also separate production and testing directories
sys.path.append('/path/to/production/code')
sys.path.append('/path/to/testing/code')

# Import a module from the specified directories
import your_module  # Replace with your actual module
