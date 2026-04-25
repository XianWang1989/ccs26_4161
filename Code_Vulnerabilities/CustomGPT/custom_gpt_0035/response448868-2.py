
import sys
import os

# Ensure package path is in sys.path
sys.path.append(r'C:/Users/.../Documents/maya/2014-x64/scripts')

# Import the package
import swapPackage.swap as swap

# Use the function
reload(swap)
swap.printSomething()
