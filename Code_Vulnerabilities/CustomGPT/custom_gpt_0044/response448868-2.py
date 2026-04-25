
# In Maya's Script Editor
import sys
print(sys.path)  # Verify your paths

# Now try importing the module
import swap
reload(swap)  # For reloading the module

# Call the function
swap.printSomething()  # This should work if everything is correct
