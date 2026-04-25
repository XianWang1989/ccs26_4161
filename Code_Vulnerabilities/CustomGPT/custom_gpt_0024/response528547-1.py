
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Convert the string representation of the bytes to actual bytes
b = eval(a)

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
