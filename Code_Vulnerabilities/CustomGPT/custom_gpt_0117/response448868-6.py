
import sys
import importlib

# Verify your path
for path in sys.path:
    print(path)

import swapPackage.swap as swap
importlib.reload(swap)
swap.printSomething()  # Should print: Hello from swapPackage.swap!
