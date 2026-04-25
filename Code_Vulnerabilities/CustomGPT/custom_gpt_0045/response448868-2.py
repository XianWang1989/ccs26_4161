
# The simple import
import swap

# If you make changes to swap.py while Maya is running, you can reload it.
from importlib import reload
reload(swap)

# Call the function defined in swap.py
swap.printSomething()
