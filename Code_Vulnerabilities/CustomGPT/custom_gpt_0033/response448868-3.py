
import sys

# Check if path is correct
for pythonPath in sys.path:
    print(pythonPath)

import swap  # Make sure the file is named swap.py
reload(swap)  # Reload the module if it's already imported
swap.printSomething()  # Call the function
