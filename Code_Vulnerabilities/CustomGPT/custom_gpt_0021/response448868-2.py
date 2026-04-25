
import sys
print("Current Python Path:")
for pythonPath in sys.path:
    print(pythonPath)

# Adjust your import statements correctly
import swap  # Ensure this file is correctly placed and recognized
reload(swap)  # Use this if you're updating swap.py during the session
swap.printSomething()  # Call the function defined in swap.py
