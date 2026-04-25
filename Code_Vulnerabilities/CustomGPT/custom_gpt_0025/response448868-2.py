
# Ensure your script is properly set up
# swap.py
def printSomething():
    print("Hello from swap!")

# In Maya's script editor
import sys
import swap  # Make sure this is the correct path

# Check if the function exists in the module
if hasattr(swap, 'printSomething'):
    reload(swap)  # Reload the module to reflect any changes
    swap.printSomething()
else:
    print("Function printSomething not found in swap module.")
