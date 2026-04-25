
import sys
print(sys.path)  # Check if the scripts path is included
from swapPackage import swap
reload(swap)
swap.printSomething()
