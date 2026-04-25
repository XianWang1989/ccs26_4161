
import sys

# Check if the path is correctly set
for pythonPath in sys.path:
    print(pythonPath)

# Import the swap module
import swap
reload(swap)
swap.printSomething()
