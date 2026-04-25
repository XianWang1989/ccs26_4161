
# -*- coding: utf-8 -*-
import sys

# Get the input argument
a = sys.argv[1]

# Convert the string representation of the bytes into actual bytes
b = eval(a)  # Use eval to interpret the literal string as a byte literal

# Print the original string and the byte representation
print(a)
print('\n')
print(b)
