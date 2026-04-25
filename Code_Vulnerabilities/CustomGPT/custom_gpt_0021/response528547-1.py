
# -*- coding: utf-8 -*-
import sys

# Take input from command line
a = sys.argv[1]

# Decode the string representation of the bytes
b = eval(a)  # Use eval to convert the input string to bytes

print(a)  # Original string
print('\n')
print(b)  # Bytes representation
