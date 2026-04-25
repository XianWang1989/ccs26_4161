
# Importing the simple script
import swap
reload(swap)
swap.printSomething()  # This should work if no naming conflicts.

# Importing from the package
import swapPackage.swap as swap
reload(swap)
swap.printSomething()  # This should also work.
