
import sys

# Check if the path is correctly set
for pythonPath in sys.path:
    print(pythonPath)  # Confirm that your swap.py location is included

# Try importing the swap module
import swap
reload(swap)
swap.printSomething()  # Ensure this runs without error
