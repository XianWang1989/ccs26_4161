
import sys
if 'swap' in sys.modules:
    del sys.modules['swap']  # Clear any existing module

# Import your module
import swap
reload(swap)  # Reload to ensure you have the latest version
swap.printSomething()  # Call your function
