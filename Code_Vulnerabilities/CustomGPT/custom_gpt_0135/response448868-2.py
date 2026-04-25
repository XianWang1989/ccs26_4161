
import sys

# Check the paths
for pythonPath in sys.path:
    print(pythonPath)

# Import and use the module
import swap
reload(swap)  # If running in Maya 2016 or earlier
swap.printSomething()
