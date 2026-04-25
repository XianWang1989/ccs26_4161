
# In Maya's Python script editor
import sys
import swap  # Ensure 'swap.py' is in the script directory

reload(swap)  # Reload the module if it's changed
swap.printSomething()  # Call the function
