
# swap.py
def printSomething():
    print("Hello from the swap module!")

# package structure should be like this:
# C:/Users/.../Documents/maya/2014-x64/scripts/swapPackage/
# ├── __init__.py
# └── swap.py

# In Maya's script editor
import swapPackage.swap as swap
reload(swap)
swap.printSomething()  # This will now work correctly
