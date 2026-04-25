
# In C:/Users/..../Documents/maya/2014-x64/scripts/swap.py
def printSomething():
    print("Hello from swap!")

# In C:/Users/..../Documents/maya/2014-x64/scripts/swapPackage/swap.py
def printSomething():
    print("Hello from swapPackage!")

# Maya Script Editor
from importlib import reload

# Loading the simple module
import swap
reload(swap)
swap.printSomething()  # Should print: Hello from swap!

# Loading the package module
import swapPackage.swap as swap
reload(swap)
swap.printSomething()  # Should print: Hello from swapPackage!
