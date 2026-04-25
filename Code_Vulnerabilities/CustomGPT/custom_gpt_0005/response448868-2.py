
# Script Editor in Maya
import sys

# Confirm the path
for pythonPath in sys.path:
    print(pythonPath)

# Import the module
import swap
reload(swap)
swap.printSomething()  # This should work now
