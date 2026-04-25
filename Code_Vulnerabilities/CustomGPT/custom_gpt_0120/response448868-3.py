
# In Maya Script Editor
import sys

# Check if the path is set correctly
for pythonPath in sys.path:
    print(pythonPath)

import swap
reload(swap)
swap.printSomething()  # This should work if defined correctly
