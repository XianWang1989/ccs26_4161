
import sys
print("Python Path:")
for pythonPath in sys.path:
    print(pythonPath)

# Attempting to import and use the module
try:
    import swap
    reload(swap)
    swap.printSomething()
except AttributeError as e:
    print(f"Error: {e}. Ensure 'printSomething' is defined in swap.py.")
