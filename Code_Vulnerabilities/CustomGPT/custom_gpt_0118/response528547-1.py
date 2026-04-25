
# -*- coding: utf-8 -*-
import sys

# Get the input from command line arguments
a = sys.argv[1]

# Convert the string representation of bytes to an actual bytes object
b = eval(a)

# Print original string and the bytes representation
print(a)
print('\n')
print(b)
