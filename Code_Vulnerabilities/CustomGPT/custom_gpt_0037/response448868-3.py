
import sys
print("Sys.path:")
for pythonPath in sys.path:
    print(pythonPath)

# Importing the module from a package
import swapPackage.swap as swap  # Importing from the package
reload(swap)  # Similar reload process
swap.printSomething()
