
import sys

# Check paths
for pythonPath in sys.path:
    print(pythonPath)

# Importing swap directly
import swap
reload(swap)  # For reloading in Maya (if needed)

# Call the function
swap.printSomething()
