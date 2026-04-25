
# Importing from scripts directory
import swap
reload(swap)
swap.printSomething()

# Importing from package
import swapPackage.swap as swap
reload(swap)
swap.printSomething()
