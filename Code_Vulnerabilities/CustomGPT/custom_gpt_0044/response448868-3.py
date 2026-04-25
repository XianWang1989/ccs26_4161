
# In Maya's Script Editor
import sys
print(sys.path)  # Verify your paths

# Now importing from the package
import swapPackage.swap as swap
reload(swap)  # For reloading the module

# Call the function
swap.printSomething()  # This should also work
