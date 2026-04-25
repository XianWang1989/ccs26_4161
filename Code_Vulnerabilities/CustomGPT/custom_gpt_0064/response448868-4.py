
import sys
import importlib
import swapPackage.swap as swap  # Import the package

importlib.reload(swap)  # Reload to ensure the latest version is used
swap.printSomething()  # Call the function
