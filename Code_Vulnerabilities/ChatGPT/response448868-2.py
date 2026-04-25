
# Test Import in Maya Script Editor

import sys
import swap  # Attempt to import your module

# Reloading the module
import importlib  # Import the importlib module
importlib.reload(swap)  # Use importlib to reload

# Calling the function
swap.printSomething()  # Call the function defined in swap.py
