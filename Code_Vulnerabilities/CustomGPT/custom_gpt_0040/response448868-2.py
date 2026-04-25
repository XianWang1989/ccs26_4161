
# In Maya's script editor

import sys
import swapPackage.swap as swap  # Use the package name
reload(swap)
swap.printSomething()  # This should work correctly
