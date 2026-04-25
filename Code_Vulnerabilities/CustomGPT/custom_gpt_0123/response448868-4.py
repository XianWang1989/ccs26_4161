
# In Maya script editor
import sys
for p in sys.path:
    print(p)  # Check your paths to ensure swapPackage is there.

import swapPackage.swap as swap
reload(swap)  # Reload the module if you've made changes
swap.printSomething()  # Call the function
