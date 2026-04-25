
# -*- coding: utf-8 -*-
import sys

# Take input from command line
a = sys.argv[1]

# Convert the string representation of bytes to actual bytes
b = eval(a)  # This safely evaluates the byte string

# Print both the original string and its byte representation
print(a)  # Original input
print('\n')
print(b)  # Byte representation
