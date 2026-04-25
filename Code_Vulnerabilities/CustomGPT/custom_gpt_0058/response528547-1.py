
# -*- coding: utf-8 -*-
import sys

# Get the input string from command line
a = sys.argv[1]

# Convert the string representation of the bytes to actual bytes
b = eval(a)  # This will treat the input as Python expression and convert to bytes

# Print the original string and the bytes
print(a)
print('\n')
print(b)
