
import sys
for path in sys.path:
    print(path)

import swapPackage.swap as swap
reload(swap)
swap.printSomething()
