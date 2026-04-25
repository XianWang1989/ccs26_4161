
# -*- coding: utf-8 -*-
import sys

# Take the input string from command line
a = sys.argv[1]

# Convert the string to bytes
# Use `bytes` with the correct escape sequences
b = eval(a)

# Print the original string and its byte representation
print(a)  # Original input
print('\n')
print(b)  # Byte representation
