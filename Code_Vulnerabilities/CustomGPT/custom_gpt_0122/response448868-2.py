
import sys
import swap
import importlib  # Use importlib for reload in Python 3

# Reload the module
importlib.reload(swap)

# Call the function
swap.printSomething()
