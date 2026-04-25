
import sys
import importlib

# Verify your path
for path in sys.path:
    print(path)

# Import and use the module
import swap
importlib.reload(swap)
swap.printSomething()  # Should print: Hello from swap!
