
# In the script editor
import sys
import swap  # Make sure swap.py is in the scripts directory
import importlib  # Use importlib for reloading in Python 3

# Reloading the module
importlib.reload(swap)

# Call the function
swap.printSomething()
