
import sys

# Checking if the path includes the scripts directory
for pythonPath in sys.path:
    print(pythonPath)

# Importing and using the module
import swap  # Ensure swap.py is in C:/Users/..../Documents/maya/2014-x64/scripts
reload(swap)
swap.printSomething()
