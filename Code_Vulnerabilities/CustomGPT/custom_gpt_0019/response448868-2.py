
import sys
print(sys.path)  # Verify your path includes your scripts directory

import swapPackage.swap as swap
reload(swap)  # Ensure the latest version is loaded
swap.printSomething()  # Call the function
