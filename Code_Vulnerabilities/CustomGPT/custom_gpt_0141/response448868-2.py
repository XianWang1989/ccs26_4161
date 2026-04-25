
# Script Editor in Maya
import sys

# Confirming the path
print("Current Python Path:")
for path in sys.path:
    print(path)

# Importing and using the module
import swap      # Make sure this matches the file name without the .py
reload(swap)
swap.printSomething()  # Should print "Hello from swap!"
