
import sys
import maya.standalone  # Required for script execution context

maya.standalone.initialize(name='python')

# Make sure to set up the import paths correctly
sys.path.append('C:/Users/..../Documents/maya/2014-x64/scripts/swapPackage')

import swap
reload(swap)  # Reload the module to reflect any changes
swap.printSomething()  # Call the function
