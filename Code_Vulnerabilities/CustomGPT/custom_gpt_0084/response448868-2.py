
import sys

# Verify the scripts directory is in sys.path
for pythonPath in sys.path:
    print(pythonPath)

# Attempt to import and use the swap module
try:
    import swap
    reload(swap)  # Make sure to use reload if you're making changes
    swap.printSomething()
except AttributeError as e:
    print("An error occurred:", e)
