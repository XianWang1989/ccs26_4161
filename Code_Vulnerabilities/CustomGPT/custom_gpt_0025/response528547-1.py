
# -*- coding: utf-8 -*-
import sys

# Get command line argument
a = sys.argv[1]

# Convert to bytes
b = bytes(a, 'utf-8')

# Print original string
print(a)
print('\n')

# Print bytes representation
print(b)
