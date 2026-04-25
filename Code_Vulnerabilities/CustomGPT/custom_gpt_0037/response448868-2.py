
import sys
print("Sys.path:")
for pythonPath in sys.path:
    print(pythonPath)

# Importing the module
import swap  # Make sure swap.py is in the scripts directory
reload(swap)  # Only needed if you change the module
swap.printSomething()
