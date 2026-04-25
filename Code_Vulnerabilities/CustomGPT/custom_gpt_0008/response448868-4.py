
# swap.py or swapPackage/swap.py
def printSomething():
    print("Hello from swap!")

# In Maya Script Editor
import sys
for pythonPath in sys.path:
    print(pythonPath)

# Direct import
import swap  # use this if swap.py is in the scripts folder
reload(swap)
swap.printSomething()

# OR for package
import swapPackage.swap as swap  # use this if inside swapPackage
reload(swap)
swap.printSomething()
