
import sys
import swapPackage.swap as swap  # Ensure proper package and module paths

try:
    # Reload the module if it's already imported
    reload(swap)
except NameError:
    # If 'reload' is not found, that means we're in Python 3 (reload is built-in)
    from importlib import reload
    reload(swap)

swap.printSomething()  # This should work correctly now
