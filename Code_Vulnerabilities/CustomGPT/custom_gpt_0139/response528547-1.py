
# -*- coding: utf-8 -*-
import sys

# Read the first argument from the command line
a = sys.argv[1]

# Convert the string literal to bytes using 'unicode_escape' to interpret escape sequences
b = bytes(a, 'utf-8').decode('unicode_escape').encode('latin1')

# Print the original string
print(a)
print('\n')

# Print the bytes representation
print(b)
