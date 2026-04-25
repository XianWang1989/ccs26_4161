
# -*- coding: utf-8 -*-
import sys

# Get input from command line
a = sys.argv[1]

# Convert the input string to bytes
b = bytes(a, 'utf-8')  # Use bytes() for the correct conversion

# Print original string and the byte representation
print(a)
print('\n')
print(b)
