
# In C:/Users/..../Documents/maya/2014-x64/scripts/swapPackage/swap.py
def printSomething():
    print("Hello from swap!")

# In Maya's script editor
import sys
sys.path.append("C:/Users/..../Documents/maya/2014-x64/scripts/swapPackage")

import swapPackage.swap as swap
reload(swap)
swap.printSomething()
