
import sys

# Check paths
for pythonPath in sys.path:
    print(pythonPath)

# Import your module
import swap

# Reload if necessary
reload(swap)

# Call the function
swap.printSomething()
