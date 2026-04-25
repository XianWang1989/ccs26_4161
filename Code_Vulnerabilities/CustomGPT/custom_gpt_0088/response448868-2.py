
import sys
import swap  # Ensure swap.py is in the directory you checked

# Reloading the swap module
import importlib
importlib.reload(swap)

# Calling the function
swap.printSomething()
