
import sys
# Check if the path is correct
for pythonPath in sys.path:
    print(pythonPath)

# Import the swap module from the package
import swapPackage.swap as swap

# Reload the module if needed
reload(swap)

# Call the function
swap.printSomething()
