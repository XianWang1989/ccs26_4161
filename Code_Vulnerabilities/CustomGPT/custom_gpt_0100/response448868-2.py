
# Ensure the package is imported correctly
import sys
import os

# Add the scripts directory to sys.path if not already included
if 'C:/Users/.../Documents/maya/2014-x64/scripts' not in sys.path:
    sys.path.append('C:/Users/.../Documents/maya/2014-x64/scripts')

# Importing from the package
import swapPackage.swap as swap
reload(swap)
swap.printSomething()
