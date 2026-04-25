
# In Maya's script editor
import sys

# Verify that the path is correct
for pythonPath in sys.path:
    print(pythonPath)

# Import and test the function
import swap  # Make sure your file is named swap.py
reload(swap)  # Reload the module to ensure you have the latest version
swap.printSomething()  # This should work if the above function is defined
