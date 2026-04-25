
# In the script editor
import sys
import importlib

# Importing from the package
import swapPackage.swap as swap

# Reloading the module
importlib.reload(swap)

# Call the function
swap.printSomething()
