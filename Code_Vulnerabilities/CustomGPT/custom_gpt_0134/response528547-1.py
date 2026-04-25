
# -*- coding: utf-8 -*-
import sys

# Read input
a = sys.argv[1]

# Convert the string representation of bytes to actual bytes
b = eval(a)  # Use eval to convert string representation to bytes

print(a)
print('\n')
print(b)
