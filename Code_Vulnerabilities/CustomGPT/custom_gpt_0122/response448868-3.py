
import sys
import swapPackage.swap as swap
import importlib

# Reload the module
importlib.reload(swap)

# Call the function
swap.printSomething()
