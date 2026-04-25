
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Convert the string to bytes; for encrypted data, this is usually direct
b = bytes(a, 'latin1')

# Print the original string and its byte representation
print(a)
print('\n')
print(b)
