
import sys

# Check the paths
for pythonPath in sys.path:
    print(pythonPath)

# Import and use the package
import swapPackage.swap as swap
reload(swap)
swap.printSomething()
