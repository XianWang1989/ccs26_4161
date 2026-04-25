
# For the standalone module
import swap
reload(swap)
swap.printSomething()  # Ensure this function exists in swap.py

# For the package
import swapPackage.swap as swap
reload(swap)
swap.printSomething()  # This should work since it's in the package
