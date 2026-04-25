
# -*- coding: utf-8 -*-
import sys

# Read input from command line
a = sys.argv[1]

# Convert the byte literal string to actual bytes
# Using 'bytes' function to interpret the escaped characters
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

# Print the original string
print(a)
print('\n')

# Print the bytes representation
print(b)
