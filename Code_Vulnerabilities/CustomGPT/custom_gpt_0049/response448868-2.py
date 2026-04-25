
import sys
print("Current Python Paths:")
for pythonPath in sys.path:
    print(pythonPath)

# Importing the module from the package
import swapPackage.swap as swap
reload(swap)  # Use reload only in interactive sessions
swap.printSomething()
