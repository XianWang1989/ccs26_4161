
# In Maya's script editor
import sys

# Check sys.path to ensure your scripts directory is included
for pythonPath in sys.path:
    print(pythonPath)

# Import and use your swap module
import swap
swap.printSomething()

# Reload if you've made changes
from importlib import reload
reload(swap)
