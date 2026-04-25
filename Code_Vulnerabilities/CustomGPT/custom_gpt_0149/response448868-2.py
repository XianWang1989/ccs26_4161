
import sys
for path in sys.path:
    print(path)  # Ensure the path is correct

import swapPackage.swap as swap
reload(swap)  # Reload the module if needed
swap.printSomething()  # Call the function
