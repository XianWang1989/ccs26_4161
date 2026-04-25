
import sys
# Check Python path
for pythonPath in sys.path:
    print(pythonPath)

# Ensure you have the correct script name
import swap  # If renamed to swap.py
reload(swap)  # If you're using Python 2; use importlib.reload(swap) in Python 3
swap.printSomething()
