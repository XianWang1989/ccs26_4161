
import sys
print("Python Paths:")
for path in sys.path:
    print(path)

# Importing from the root
import swap
swap.printSomething()  # This should work

# Importing from the package
import swapPackage.swap as swap_pkg
swap_pkg.printSomething()  # This should also work
