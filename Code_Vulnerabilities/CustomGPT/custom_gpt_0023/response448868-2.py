
import sys
print("Paths:")
for path in sys.path:
    print(path)

# Try to import
import swap
reload(swap)  # For Python 2.x, otherwise use `importlib.reload` in Python 3
swap.printSomething()
