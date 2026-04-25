
import sys
import swapPackage.swap as swap  # Use the package name to avoid conflicts

reload(swap)  # Reload to ensure any changes are picked up
swap.printSomething()  # Call your function
