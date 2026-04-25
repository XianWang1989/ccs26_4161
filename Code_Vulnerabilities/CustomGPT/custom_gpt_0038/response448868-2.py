
import sys
import maya.utils

# Ensure the path is included for loading packages
sys.path.append('C:/Users/..../Documents/maya/2014-x64/scripts/swapPackage')

# Now import your module
import swapPackage.swap as swap

# Reload if necessary (not always required)
maya.utils.executeDeferred("reload(swap)")

# Call the function
swap.printSomething()
