
import sys
import swapPackage.swap as swap

# Reload module if it's already imported
import importlib
importlib.reload(swap)

# Call the function
swap.printSomething()
