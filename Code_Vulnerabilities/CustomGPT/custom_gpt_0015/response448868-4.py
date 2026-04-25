
# In C:/Users/..../Documents/maya/2014-x64/scripts/swap.py
def printSomething():
    print("Hello from swap!")

# In Maya's script editor
import sys
sys.path.append("C:/Users/..../Documents/maya/2014-x64/scripts")  # Add the path if it's not there

import swap  # Ensure it's recognized
import importlib
importlib.reload(swap)  # Reload module for changes
swap.printSomething()  # This should work now
