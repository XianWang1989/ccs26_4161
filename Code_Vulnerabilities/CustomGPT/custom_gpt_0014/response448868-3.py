
import sys

# Print current Python paths
for pythonPath in sys.path:
    print(pythonPath)

# Import the module
import swap
reload(swap)
swap.printSomething()  # Should output: Hello from swap!
